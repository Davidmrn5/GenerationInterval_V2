import sys
sys.path.append('/faststorage/project/genint2_develop/GenerationInterval_V2/src')

import panel as pn
import time
from assets.variables import *
from tools.sta_ind.utils import *
import holoviews as hv

hv.extension("bokeh")
def app_instance():
    var = GeneralVariables()
    sta_var = StaIndVariables()

    # Widgets
    dim_sel = pn.widgets.RadioButtonGroup(
        name="Dimension selector", options=var.dims, button_type="light"
    )

    plot_selector = pn.widgets.Select(name="Plot selector", groups=var.plots1D)

    datas_1 = pn.widgets.MultiChoice(placeholder="Dataset dim 1", options=var.datasets)
    regs_1 = pn.widgets.MultiChoice(placeholder="Region dim 1", options=var.regions)
    mpp_1 = pn.widgets.IntSlider(value=50, start=50, end=95, step=5)
    chrms_1 = pn.widgets.MultiChoice(
        placeholder="Chromosomes dim 1", options=var.disc_chrom
    )
    ancs_1 = pn.widgets.MultiChoice(placeholder="Ancestry dim 1", options=var.ancestries)


    datas_2 = pn.widgets.MultiChoice(
        placeholder="Dataset dim 2", options=var.datasets, visible=False
    )
    regs_2 = pn.widgets.MultiChoice(
        placeholder="Region dim 2", visible=False, options=var.regions
    )
    mpp_2 = pn.widgets.IntSlider(value=50, start=50, end=95, step=5, visible=False)
    chrms_2 = pn.widgets.MultiChoice(
        placeholder="Chromosomes dim 2", options=var.disc_chrom, visible=False
    )
    ancs_2 = pn.widgets.MultiChoice(
        placeholder="Ancestry dim 2", options=var.ancestries, visible=False
    )

    var_1 = pn.widgets.Select(name="Dimension 1 variable", options=sta_var.plot_vars)
    facet_1 = pn.widgets.MultiChoice(name="Dimension 1 facet", options=sta_var.plot_facets)
    var_2 = pn.widgets.Select(
        name="Dimension 2 variable", options=sta_var.plot_vars, visible=False
    )
    facet_2 = pn.widgets.MultiChoice(
        name="Dimension 2 facet", options=sta_var.plot_facets, visible=False
    )
    color = pn.widgets.MultiChoice(name="Color by:", options=sta_var.colors)

    data_load_but = pn.widgets.Button(name="Load data!", button_type="light")

    list_widgets_1 = [datas_1, regs_1, mpp_1, chrms_1, ancs_1, var_1, facet_1]
    list_widgets_2 = [datas_2, regs_2, mpp_2, chrms_2, ancs_2, var_2, facet_2]

    widgets_1 = pn.Row(datas_1, regs_1, mpp_1, chrms_1, ancs_1)
    widgets_2 = pn.Row(datas_2, regs_2, mpp_2, chrms_2, ancs_2)
    plot_options = pn.Row(var_1, var_2, facet_1, facet_2, color, plot_selector)


    # Selected dimension
    @pn.depends(dimension=dim_sel, watch=True)
    def _selecteddim(dimension):
        if dim_sel.value == "1D Plot":
            plot_selector.groups = var.plots1D
            for widget in list_widgets_2:
                widget.visible = False
        else:
            plot_selector.groups = var.plots2D
            for widget in list_widgets_2:
                widget.visible = True


    # Data loading and plotting
    @pn.depends(but_press=data_load_but)
    def _loaddata(but_press):
        if but_press:
            time0 = time.time()
            if dim_sel.value == "1D Plot":
                lazy_dim1, df_dim1 = filter_ind_stat_1d(
                    datas_1.value, mpp_1.value, regs_1.value, ancs_1.value, chrms_1.value
                )
                if plot_selector.value == "Violin":
                    violin_plot = plot_violin(
                        lazy_dim1, var_1.value, facet_1.value, color.value
                    )
                    layout[1] = violin_plot

            elif dim_sel.value == "2D Plot":
                df_dim1, df_dim2, df_joined = filter_ind_stat_2d(
                    datas_1.value,
                    mpp_1.value,
                    regs_1.value,
                    ancs_1.value,
                    chrms_1.value,
                    datas_2.value,
                    mpp_2.value,
                    regs_2.value,
                    ancs_2.value,
                    chrms_2.value,
                )
            time1 = time.time()
            elapsed_time = f"{time1-time0} seconds"
            return "Data & plot loaded in", elapsed_time
        else:
            return "Data not loaded yet"


    layout = pn.Column(
        pn.Column(
            dim_sel, pn.Column(widgets_1, widgets_2), plot_options, data_load_but, _loaddata
        ),
        pn.panel("", sizing_mode="stretch_both"),
    )

    return layout.servable()
