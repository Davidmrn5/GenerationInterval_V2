Stuff to optimize: data wrangling is done for plot and table when df is the same

    Functions:
    out_co2
        get_co2_df
            list_ind   
            load_indstat_fragments
                load_meta

    Needs: variables.R

    Gets variables as a source, there will be datasets etc.

    DATA (on click)
        (Excludes) Put in list_ind individuals selected on text & selected on tree. (only individual names as name_DATASET)
            
            list_ind function:

        Uses load_indstat_fragments with input mean posterior probability.
            
            load_indstat_fragments function:
                Iterates though each dataset with said mean posterior probability. (format DATASET_MPP_perind.txt).
                Names columns ("ind", "dat", "chrom", "anc", "hap", "len_mea", "len_med", "len_max", "len_min", "nfr", "seq")
                Concatenates in rows.
                
                load_meta function:
                Reads moi/files/metadata.txt (has ind	sex	pop	reg	dat	oda	tim	lat	lon	cre	cda as headers) and takes those individuals whose dat is part of the variables datasets.
                Creates a new column that formats ind_dat named lin.

                Joins metadata corresponoding to individuals and datasets
                Reads moi/sandbox/adm/ALL/ALL.ind and assings columns "ind", "sex", "regdat" and selects ONLY ind
                Joins by individual the data from sandbox/adm/ALL/ALL.6.Q with columns "ancAMR", "ancEAS", "ancSAS", "ancAFR", "ancEUR", "ancOCE"
                Returns a df with columns ind, dat, lin, oda, sex, pop, reg, hap, anc, tim, lat, lon, cre, cda, chrom, len_mea, len_med, len_max, len_min, nfr, seq, ancAFR, ancAMR, ancEAS, ancEUR, ancOCE, ancSAS
                
        From the df of load_indstat fragments excludes ind_dat present in list_ind
        Filters df based on dat and reg and takes to df again, returns df.

Plotting: 

    At button click notify abour corr plot
    Stop plot null

    defines variable s as 11 USED FOR PADDING
    Loads data
    group_means vector with "col" name only
    Filters df based on chromosome and ancestry.

----Xaxis definitiion
    Creates "x" on df which are values of the variables that you can plot in x axis (all columns present in df)

----Yaxis definition
    If we are plotting 2D we add to "y" column the second variable.

----Color definition
    Color input (multiple choice) based on each of the columns
        If 1 input, creates new column named col that takes values of the selected input in multiple choice
        Elif non 0 inputs, creates col which will be a joined of the selected values with_
        If 0 inputs col is a point

----Facet definition
    Checks if we want facets (length selection)
        Creates new column called facet_y that appends all values of the options with _
        Adds facet_y to vector group_means
    Does the same for facet_x

----Plot correlations
  --1D
    Histogram (needs bins selector)
        Normal histogram, fill and boxes are with color defined in col color, X values and number of defined bins with defined alpha.

    Violin
        Groups by each word of group_means (we were appending here col as well as facet_x or facet_y if selected).
        Mean of x for each of the groups
        Ungroups and regroups only by col
        Takes the mean of the means before for each col group.
        Ascending mean order
        Extracs the values of color and assigns to variable group order in ascending mean order for each "color"

        converts color to a number ordered by color order
        color based on col column
        violin plot being in x axis color and y axis values of X with alpha 0.2 median line.

        Adds jittered points (sme values as violin) with the tooltips Ind, Sex, Dataset, Region, Population, Chromosome, Haplotype and X var

    Density
        density plot, fill and color, X values and alpha

    Bar
        bar plot, fill and color, X values and alpha
    
  --2D
    point
        point plot with fill and edge color as col, then point being x x and y y, Tooltip with Ind, Sex, Dataset, Region, Population, Chromosome, Haplotype, X var and Y var.
        If chosen to use linear model:
            For each vale of group_means (color+facets) groups the dataframe based on those columns
            Min and max of x values for each group

            Paralel, groups agains the same way, then linear model of y on x for each group, renames coefficients as intercept and slope, they become column names and writes the intercept and slope as values within the column, then ungroups.

            Joins both dataframes,
            Calculates the min y and max y as a function of intercept slope and min x and max x calculated before and puts it as columns.

            Sums the point plot before to a smoothed line using linear regression of x and y. Adds interactive segment (line) with data segments (dataframe of before), gets min x and min y starting points and max x and max y as ending points. For the tooltip it writes the y=ax+b equiation.

    2D density (needs bins selector)
        2D density plot using standard x and y with bins, no color used.

    quantiles
        For each vale of group_means (color+facets) groups the dataframe based on those columns
        Ascending order of x for each group
        New column q, each value will be a quantile (based on quantiles provided)
        Ungroups data
        Regroups by every value in group_means and quantiles
        Calculates, for each y mean median, max, min, sd  and for x max and min as well as counts for each groups
        Turns the x value to the quantiles.
        Puts into a column stat name and y column the values of each stat.
        Eliminates rows with stats not selected by user
        Plots a line with fill and outline with x and y, the type of line (dashed etc) is defined by the stats.
        Plots points with x and y, tooptip is stat, number of fragment, Y value, X range

----Plot means
    If we want to show mean of x
        if the plot is violin
            Adds to the plot interactive error bars. Data is:
            Grouping by selected group_means, the get the mean of x for each group, and getting standard error (formula)
            For x is color, y minimum is mean-standard error, ymax is mean + standard error, with tooltip that tells the standard error.
            Adds interactive points, does the same but puts the y as mean for each group and the tooltip will be mean.

        if the plot is NOT violin
            Creates vertical line, groups by the group_means and for each group is calculates mean and median of x, then expands to columns stat and value and sets intercept on x to value (median/mean) being the type of line the stat plotted, color color and as tooltip the stat it is with its value
    If we have 1d2d as false (2d chosen) and want mean of y
        Creates horizontal line, groups by the group_means and for each group is calculates mean and median of y, then expands to columns stat and value and sets intercept on y to value (median/mean) being the type of line the stat plotted, color color and as tooltip the stat it is with its value

----Defines x and y limits for the plots

----Facets
    If we have facet y and x we do that with the plot based on scale and spacing
    If we only facet y or x, same only for y or x.

----Axis labels
    If plot violin adds label to y axis
    If plot not violin x label to x axis and y label to x axis.

----Color scales
    If plot not 2D density
        If only 1 color and discrete (ancestry, region, dataset) manual scale
        If only 1 color and conitnous (lot of variables)
        continous (viridis) scale.

----Finishes with some aesthetics for the plot.

Text below with excluded individuals

Table: It wrangles again the data, sharing the dataframe would be more efficient I guess.

    Gets data, same way it was done for plotting, at go lists individuals, and load indstat fragments

    Filters by dataset and region and places the dataframe

    Renders a table with the data
    If no rows table is null. Then pipes the table into a datatable with options to search, sort, copy and export as csv, excel, pdf or print.