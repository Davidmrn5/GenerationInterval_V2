# conda activate playground_polars

import polars as pl
import time
import pandas as pd
import holoviews as hv
from holoviews import opts, dim
from bokeh.models import (
    Scatter,
    PanTool,
    PrintfTickFormatter,
    HoverTool,
    ColumnDataSource,
    CDSView,
    GroupFilter,
)
from bokeh.transform import jitter
from bokeh.layouts import row, layout


def combine_all():
    all6_lzframe = pl.scan_csv(
        "/faststorage/project/genint2_develop/GenerationInterval_V2/data/adm/ALL.6.Q",
        new_columns=["ancAMR", "ancEAS", "ancSAS", "ancAFR", "ancEUR", "ancOCE"],
        has_header=False,
        separator=" ",
        dtypes=[
            pl.Float64,
            pl.Float64,
            pl.Float64,
            pl.Float64,
            pl.Float64,
            pl.Float64,
        ],
    )
    all_lzframe = pl.scan_csv(
        "/faststorage/project/genint2_develop/GenerationInterval_V2/data/adm/ALL.ind",
        has_header=False,
        separator="\t",
        new_columns=["ind", "sex", "regdat"],
        dtypes=[
            pl.Utf8,
            pl.Utf8,
            pl.Utf8,
        ],
    ).select("ind")
    combined_all = pl.concat([all_lzframe, all6_lzframe], how="horizontal")
    return combined_all


def filter_ind_stat_1d(datas_dim1, mpp_dim1, regs_dim1, ancs_dim1, chrms_dim1):

    meta = pl.scan_csv(
        "/faststorage/project/genint2_develop/GenerationInterval_V2/data/meta/metadata.txt",
        has_header=True,
        separator="\t",
        schema={
            "ind": pl.Utf8,
            "sex": pl.Utf8,
            "pop": pl.Utf8,
            "reg": pl.Utf8,
            "dat": pl.Utf8,
            "oda": pl.Utf8,
            "tim": pl.Int64,
            "lat": pl.Float64,
            "lon": pl.Float64,
            "cre": pl.Utf8,
            "cda": pl.Utf8,
        },
    ).with_columns((pl.col("ind") + "_" + pl.col("dat")).alias("lin"))
    combined_all = combine_all()

    queries_dim1 = []
    for data_dim1 in datas_dim1:
        q = pl.scan_csv(
            f"/faststorage/project/genint2_develop/GenerationInterval_V2/data/fra/{data_dim1}_{mpp_dim1}_perind.txt",
            has_header=False,
            new_columns=[
                "ind",
                "dat",
                "chrom",
                "anc",
                "hap",
                "len_mea",
                "len_med",
                "len_max",
                "len_min",
                "nfr",
                "seq",
            ],
            separator="	",
            dtypes=[
                pl.Utf8,
                pl.Utf8,
                pl.Utf8,
                pl.Utf8,
                pl.Int64,
                pl.Float64,
                pl.Float64,
                pl.Int64,
                pl.Int64,
                pl.Int64,
                pl.Int64,
            ],
            infer_schema_length=0,
        )

        queries_dim1.append(q)

    lazy_df_dim1 = (
        pl.concat(queries_dim1)
        .filter(
            pl.col("chrom").is_in(chrms_dim1),
            pl.col("anc").is_in(ancs_dim1),
        )
        .join(meta, on=["ind", "dat"])
        .filter(pl.col("reg").is_in(regs_dim1))
        .join(combined_all, on=["ind"])
    )
    df_dim1 = lazy_df_dim1.collect()

    return lazy_df_dim1, df_dim1


def filter_ind_stat_2d(
    datas_dim1,
    mpp_dim1,
    regs_dim1,
    ancs_dim1,
    chrms_dim1,
    datas_dim2,
    mpp_dim2,
    regs_dim2,
    ancs_dim2,
    chrms_dim2,
):
    meta = pl.scan_csv(
        "/faststorage/project/genint2_develop/GenerationInterval_V2/data/meta/metadata.txt",
        has_header=True,
        separator="\t",
        schema={
            "ind": pl.Utf8,
            "sex": pl.Utf8,
            "pop": pl.Utf8,
            "reg": pl.Utf8,
            "dat": pl.Utf8,
            "oda": pl.Utf8,
            "tim": pl.Int64,
            "lat": pl.Float64,
            "lon": pl.Float64,
            "cre": pl.Utf8,
            "cda": pl.Utf8,
        },
    ).with_columns((pl.col("ind") + "_" + pl.col("dat")).alias("lin"))
    combined_all = combine_all()

    queries_dim1 = []
    for data_dim1 in datas_dim1:
        q = pl.scan_csv(
            f"/faststorage/project/genint2_develop/GenerationInterval_V2/data/fra/{data_dim1}_{mpp_dim1}_perind.txt",
            has_header=False,
            new_columns=[
                "ind",
                "dat",
                "chrom",
                "anc",
                "hap",
                "len_mea",
                "len_med",
                "len_max",
                "len_min",
                "nfr",
                "seq",
            ],
            separator="	",
            dtypes=[
                pl.Utf8,
                pl.Utf8,
                pl.Utf8,
                pl.Utf8,
                pl.Int64,
                pl.Float64,
                pl.Float64,
                pl.Int64,
                pl.Int64,
                pl.Int64,
                pl.Int64,
            ],
            infer_schema_length=0,
        )

        queries_dim1.append(q)

    lazy_df_dim1 = (
        pl.concat(queries_dim1)
        .filter(
            pl.col("chrom").is_in(chrms_dim1),
            pl.col("anc").is_in(ancs_dim1),
        )
        .join(meta, on=["ind", "dat"])
        .filter(pl.col("reg").is_in(regs_dim1))
        .join(combined_all, on=["ind"])
    )

    queries_dim2 = []
    for data_dim2 in datas_dim2:
        q = pl.scan_csv(
            f"/faststorage/project/genint2_develop/GenerationInterval_V2/data/fra/{data_dim2}_{mpp_dim2}_perind.txt",
            has_header=False,
            new_columns=[
                "ind",
                "dat",
                "chrom",
                "anc",
                "hap",
                "len_mea",
                "len_med",
                "len_max",
                "len_min",
                "nfr",
                "seq",
            ],
            separator="	",
            dtypes=[
                pl.Utf8,
                pl.Utf8,
                pl.Utf8,
                pl.Utf8,
                pl.Int64,
                pl.Float64,
                pl.Float64,
                pl.Int64,
                pl.Int64,
                pl.Int64,
                pl.Int64,
            ],
            infer_schema_length=0,
        )

        queries_dim2.append(q)

    lazy_df_dim2 = (
        pl.concat(queries_dim2)
        .filter(
            pl.col("chrom").is_in(chrms_dim2),
            pl.col("anc").is_in(ancs_dim2),
        )
        .join(meta, on=["ind", "dat"])
        .filter(pl.col("reg").is_in(regs_dim2))
        .join(combined_all, on=["ind"])
    )

    df_dim1 = lazy_df_dim1.collect()
    df_dim2 = lazy_df_dim2.collect()
    df_joined = pl.concat([lazy_df_dim1, lazy_df_dim2]).collect()

    return df_dim1, df_dim2, df_joined


def color_facet_1d(df, col, fac_1):
    groups = ["col"]
    if len(col) == 0:
        df_colfac = df.with_columns(pl.lit(".").alias("col"))
    elif len(col) == 1:
        df_colfac = df.with_columns(pl.col(col).alias("col"))
    elif len(col) > 1:
        df_colfac = df.with_columns(
            pl.concat_str([pl.col(col)], separator="_").alias("col")
        )
    if len(fac_1) > 1:
        df_colfac = df_colfac.with_columns(
            pl.concat_str([pl.col(fac_1)], separator="_").alias("fac_1")
        )
        groups.append("fac_1")
    return df_colfac, groups


def plot_violin(df, var_dim1, fac_1, col):
    """
    df_dim1 needs to be lazyframe
    """
    groups = ["col"]
    if len(fac_1) > 0:
        groups.append("fac_1")
        if len(col) == 0:
            df_dim1_col = df.with_columns(pl.lit(".").alias("col")).with_columns(
                pl.concat_str([pl.col(fac_1)], separator="_").alias("fac_1")
            )
            colors_name = ""
        elif len(col) > 0:
            df_dim1_col = df.with_columns(
                pl.concat_str([pl.col(col)], separator="_").alias("col")
            ).with_columns(pl.concat_str([pl.col(fac_1)], separator="_").alias("fac_1"))
            colors_name = "_".join(col)
    else:
        if len(col) == 0:
            df_dim1_col = df.with_columns(
                pl.concat_str([pl.col(fac_1)], separator="_").alias("fac_1")
            )
            colors_name = ""
        elif len(col) > 0:
            df_dim1_col = df.with_columns(
                pl.concat_str([pl.col(fac_1)], separator="_").alias("fac_1")
            )
            colors_name = "_".join(col)
    print(df_dim1_col.collect())
    color_order = (
        df_dim1_col.select((groups + [var_dim1]))
        .group_by(groups)
        .mean()
        .select("col", var_dim1)
        .group_by("col")
        .mean()
        .sort(var_dim1)
        .select("col")
        .collect()
        .get_columns()
    )[0].to_list()

    colormap = {}
    for i, color in enumerate(color_order):
        colormap[color] = hv.Cycle("Colorblind").values[i]
    order_dict = {val: idx for idx, val in enumerate(color_order)}

    facet_list = (
        (df_dim1_col.select("fac_1").unique().sort("fac_1").collect().get_columns())[0]
    ).to_list()

    df_dim1_col = (
        df_dim1_col.sort(pl.col("col").replace(order_dict)).collect().to_pandas()
    )

    source = ColumnDataSource(df_dim1_col)

    hover_tooltips = [
        ("Ind", "@ind"),
        ("Sex", "@sex"),
        ("Data", "@dat"),
        ("Reg", "@reg"),
        ("Pop", "@pop"),
        ("Chrom", "@chrom"),
        ("Hapl", "@hap"),
    ]

    def plot_each_facet(facet_name):

        view = CDSView(filter=GroupFilter(column_name="fac_1", group=facet_name))

        single_violin = hv.Violin(
            df_dim1_col[df_dim1_col["fac_1"] == facet_name],
            kdims=("col", colors_name),
            vdims=(var_dim1, var_dim1),
        ).opts(
            show_legend=False,
            height=600,
            violin_fill_color=dim("col"),
            cmap=colormap,
            default_tools=[],
        )

        single_violin = hv.render(single_violin)

        fill = single_violin.renderers[0]
        outside_line = single_violin.renderers[1]
        whisker = single_violin.renderers[2]
        mean_point = single_violin.renderers[4]
        box = single_violin.renderers[3]

        scatter = Scatter(
            x=jitter("col", width=0.5, range=single_violin.x_range),
            y=var_dim1,
            marker="circle",
        )

        single_violin.renderers = []
        single_violin.add_glyph(source, scatter, view=view)
        single_violin.renderers.append(fill)
        single_violin.renderers.append(outside_line)

        single_violin.xaxis.axis_label = facet_name
        single_violin.toolbar.logo = None
        single_violin.add_tools(
            PanTool(dimensions="height"),
            HoverTool(tooltips=hover_tooltips, renderers=[single_violin.renderers[0]]),
        )
        single_violin.min_border = 0
        single_violin.yaxis.formatter = PrintfTickFormatter(format="%0.1e")

        return single_violin

    plot_list = [(plot_each_facet(facet_name)) for facet_name in facet_list]
    fig = layout(row(plot_list, spacing=0))
    for i in range(1, len(plot_list)):
        fig.children[0].children[i].yaxis.visible = False
        fig.children[0].children[i].x_range = fig.children[0].children[0].x_range
        fig.children[0].children[i].y_range = fig.children[0].children[0].y_range
        fig.children[0].children[i - 1].toolbar_location = None
    return fig
