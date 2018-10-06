import _plotly_utils.basevalidators


class XAxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='xaxis', parent_name='layout', **kwargs):
        super(XAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'XAxis'),
            data_docs=kwargs.pop(
                'data_docs', """
            anchor
                If set to an opposite-letter axis id (e.g.
                `x2`, `y`), this axis is bound to the
                corresponding opposite-letter axis. If set to
                "free", this axis' position is determined by
                `position`.
            automargin
                Determines whether long tick labels
                automatically grow the figure margins.
            autorange
                Determines whether or not the range of this
                axis is computed in relation to the input data.
                See `rangemode` for more info. If `range` is
                provided, then `autorange` is set to False.
            calendar
                Sets the calendar system to use for `range` and
                `tick0` if this is a date axis. This does not
                set the calendar for interpreting data on this
                axis, that's specified in the trace or via the
                global `layout.calendar`
            categoryarray
                Sets the order in which categories on this axis
                appear. Only has an effect if `categoryorder`
                is set to "array". Used with `categoryorder`.
            categoryarraysrc
                Sets the source reference on plot.ly for
                categoryarray .
            categoryorder
                Specifies the ordering logic for the case of
                categorical variables. By default, plotly uses
                "trace", which specifies the order that is
                present in the data supplied. Set
                `categoryorder` to *category ascending* or
                *category descending* if order should be
                determined by the alphanumerical order of the
                category names. Set `categoryorder` to "array"
                to derive the ordering from the attribute
                `categoryarray`. If a category is not found in
                the `categoryarray` array, the sorting behavior
                for that attribute will be identical to the
                "trace" mode. The unspecified categories will
                follow the categories in `categoryarray`.
            color
                Sets default for all colors associated with
                this axis all at once: line, font, tick, and
                grid colors. Grid color is lightened by
                blending this with the plot background
                Individual pieces can override this.
            constrain
                If this axis needs to be compressed (either due
                to its own `scaleanchor` and `scaleratio` or
                those of the other axis), determines how that
                happens: by increasing the "range" (default),
                or by decreasing the "domain".
            constraintoward
                If this axis needs to be compressed (either due
                to its own `scaleanchor` and `scaleratio` or
                those of the other axis), determines which
                direction we push the originally specified plot
                area. Options are "left", "center" (default),
                and "right" for x axes, and "top", "middle"
                (default), and "bottom" for y axes.
            domain
                Sets the domain of this axis (in plot
                fraction).
            dtick
                Sets the step in-between ticks on this axis.
                Use with `tick0`. Must be a positive number, or
                special strings available to "log" and "date"
                axes. If the axis `type` is "log", then ticks
                are set every 10^(n*dtick) where n is the tick
                number. For example, to set a tick mark at 1,
                10, 100, 1000, ... set dtick to 1. To set tick
                marks at 1, 100, 10000, ... set dtick to 2. To
                set tick marks at 1, 5, 25, 125, 625, 3125, ...
                set dtick to log_10(5), or 0.69897000433. "log"
                has several special values; "L<f>", where `f`
                is a positive number, gives ticks linearly
                spaced in value (but not position). For example
                `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                plus small digits between, use "D1" (all
                digits) or "D2" (only 2 and 5). `tick0` is
                ignored for "D1" and "D2". If the axis `type`
                is "date", then you must convert the time to
                milliseconds. For example, to set the interval
                between ticks to one day, set `dtick` to
                86400000.0. "date" also has special values
                "M<n>" gives ticks spaced by a number of
                months. `n` must be a positive integer. To set
                ticks on the 15th of every third month, set
                `tick0` to "2000-01-15" and `dtick` to "M3". To
                set ticks every 4 years, set `dtick` to "M48"
            exponentformat
                Determines a formatting rule for the tick
                exponents. For example, consider the number
                1,000,000,000. If "none", it appears as
                1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                "power", 1x10^9 (with 9 in a super script). If
                "SI", 1G. If "B", 1B.
            fixedrange
                Determines whether or not this axis is zoom-
                able. If true, then zoom is disabled.
            gridcolor
                Sets the color of the grid lines.
            gridwidth
                Sets the width (in px) of the grid lines.
            hoverformat
                Sets the hover text formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see: h
                ttps://github.com/d3/d3-format/blob/master/READ
                ME.md#locale_format And for dates see:
                https://github.com/d3/d3-time-
                format/blob/master/README.md#locale_format We
                add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            layer
                Sets the layer on which this axis is displayed.
                If *above traces*, this axis is displayed above
                all the subplot's traces If *below traces*,
                this axis is displayed below all the subplot's
                traces, but above the grid lines. Useful when
                used together with scatter-like traces with
                `cliponaxis` set to False to show markers
                and/or text nodes above this axis.
            linecolor
                Sets the axis line color.
            linewidth
                Sets the width (in px) of the axis line.
            mirror
                Determines if the axis lines or/and ticks are
                mirrored to the opposite side of the plotting
                area. If True, the axis lines are mirrored. If
                "ticks", the axis lines and ticks are mirrored.
                If False, mirroring is disable. If "all", axis
                lines are mirrored on all shared-axes subplots.
                If "allticks", axis lines and ticks are
                mirrored on all shared-axes subplots.
            nticks
                Specifies the maximum number of ticks for the
                particular axis. The actual number of ticks
                will be chosen automatically to be less than or
                equal to `nticks`. Has an effect only if
                `tickmode` is set to "auto".
            overlaying
                If set a same-letter axis id, this axis is
                overlaid on top of the corresponding same-
                letter axis. If False, this axis does not
                overlay any same-letter axes.
            position
                Sets the position of this axis in the plotting
                space (in normalized coordinates). Only has an
                effect if `anchor` is set to "free".
            range
                Sets the range of this axis. If the axis `type`
                is "log", then you must take the log of your
                desired range (e.g. to set the range from 1 to
                100, set the range from 0 to 2). If the axis
                `type` is "date", it should be date strings,
                like date data, though Date objects and unix
                milliseconds will be accepted and converted to
                strings. If the axis `type` is "category", it
                should be numbers, using the scale where each
                category is assigned a serial number from zero
                in the order it appears.
            rangemode
                If "normal", the range is computed in relation
                to the extrema of the input data. If *tozero*`,
                the range extends to 0, regardless of the input
                data If "nonnegative", the range is non-
                negative, regardless of the input data. Applies
                only to linear axes.
            rangeselector
                plotly.graph_objs.layout.xaxis.Rangeselector
                instance or dict with compatible properties
            rangeslider
                plotly.graph_objs.layout.xaxis.Rangeslider
                instance or dict with compatible properties
            scaleanchor
                If set to another axis id (e.g. `x2`, `y`), the
                range of this axis changes together with the
                range of the corresponding axis such that the
                scale of pixels per unit is in a constant
                ratio. Both axes are still zoomable, but when
                you zoom one, the other will zoom the same
                amount, keeping a fixed midpoint. `constrain`
                and `constraintoward` determine how we enforce
                the constraint. You can chain these, ie `yaxis:
                {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}`
                but you can only link axes of the same `type`.
                The linked axis can have the opposite letter
                (to constrain the aspect ratio) or the same
                letter (to match scales across subplots). Loops
                (`yaxis: {scaleanchor: *x*}, xaxis:
                {scaleanchor: *y*}` or longer) are redundant
                and the last constraint encountered will be
                ignored to avoid possible inconsistent
                constraints via `scaleratio`.
            scaleratio
                If this axis is linked to another by
                `scaleanchor`, this determines the pixel to
                unit scale ratio. For example, if this value is
                10, then every unit on this axis spans 10 times
                the number of pixels as a unit on the linked
                axis. Use this for example to create an
                elevation profile where the vertical scale is
                exaggerated a fixed amount with respect to the
                horizontal.
            separatethousands
                If "true", even 4-digit integers are separated
            showexponent
                If "all", all exponents are shown besides their
                significands. If "first", only the exponent of
                the first tick is shown. If "last", only the
                exponent of the last tick is shown. If "none",
                no exponents appear.
            showgrid
                Determines whether or not grid lines are drawn.
                If True, the grid lines are drawn at every tick
                mark.
            showline
                Determines whether or not a line bounding this
                axis is drawn.
            showspikes
                Determines whether or not spikes (aka
                droplines) are drawn for this axis. Note: This
                only takes affect when hovermode = closest
            showticklabels
                Determines whether or not the tick labels are
                drawn.
            showtickprefix
                If "all", all tick labels are displayed with a
                prefix. If "first", only the first tick is
                displayed with a prefix. If "last", only the
                last tick is displayed with a suffix. If
                "none", tick prefixes are hidden.
            showticksuffix
                Same as `showtickprefix` but for tick suffixes.
            side
                Determines whether a x (y) axis is positioned
                at the "bottom" ("left") or "top" ("right") of
                the plotting area.
            spikecolor
                Sets the spike color. If undefined, will use
                the series color
            spikedash
                Sets the dash style of lines. Set to a dash
                type string ("solid", "dot", "dash",
                "longdash", "dashdot", or "longdashdot") or a
                dash length list in px (eg "5px,10px,2px,2px").
            spikemode
                Determines the drawing mode for the spike line
                If "toaxis", the line is drawn from the data
                point to the axis the  series is plotted on. If
                "across", the line is drawn across the entire
                plot area, and supercedes "toaxis". If
                "marker", then a marker dot is drawn on the
                axis the series is plotted on
            spikesnap
                Determines whether spikelines are stuck to the
                cursor or to the closest datapoints.
            spikethickness
                Sets the width (in px) of the zero line.
            tick0
                Sets the placement of the first tick on this
                axis. Use with `dtick`. If the axis `type` is
                "log", then you must take the log of your
                starting tick (e.g. to set the starting tick to
                100, set the `tick0` to 2) except when
                `dtick`=*L<f>* (see `dtick` for more info). If
                the axis `type` is "date", it should be a date
                string, like date data. If the axis `type` is
                "category", it should be a number, using the
                scale where each category is assigned a serial
                number from zero in the order it appears.
            tickangle
                Sets the angle of the tick labels with respect
                to the horizontal. For example, a `tickangle`
                of -90 draws the tick labels vertically.
            tickcolor
                Sets the tick color.
            tickfont
                Sets the tick font.
            tickformat
                Sets the tick label formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see: h
                ttps://github.com/d3/d3-format/blob/master/READ
                ME.md#locale_format And for dates see:
                https://github.com/d3/d3-time-
                format/blob/master/README.md#locale_format We
                add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            tickformatstops
                plotly.graph_objs.layout.xaxis.Tickformatstop
                instance or dict with compatible properties
            tickformatstopdefaults
                plotly.graph_objs.layout.xaxis.Tickformatstop
                instance or dict with compatible properties
            ticklen
                Sets the tick length (in px).
            tickmode
                Sets the tick mode for this axis. If "auto",
                the number of ticks is set via `nticks`. If
                "linear", the placement of the ticks is
                determined by a starting position `tick0` and a
                tick step `dtick` ("linear" is the default
                value if `tick0` and `dtick` are provided). If
                "array", the placement of the ticks is set via
                `tickvals` and the tick text is `ticktext`.
                ("array" is the default value if `tickvals` is
                provided).
            tickprefix
                Sets a tick label prefix.
            ticks
                Determines whether ticks are drawn or not. If
                **, this axis' ticks are not drawn. If
                "outside" ("inside"), this axis' are drawn
                outside (inside) the axis lines.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on plot.ly for
                ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on plot.ly for
                tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                Sets the title of this axis.
            titlefont
                Sets this axis' title font.
            type
                Sets the axis type. By default, plotly attempts
                to determined the axis type by looking into the
                data of the traces that referenced the axis in
                question.
            visible
                A single toggle to hide the axis while
                preserving interaction like dragging. Default
                is true when a cheater plot is present on the
                axis, otherwise false
            zeroline
                Determines whether or not a line is drawn at
                along the 0 value of this axis. If True, the
                zero line is drawn on top of the grid lines.
            zerolinecolor
                Sets the line color of the zero line.
            zerolinewidth
                Sets the width (in px) of the zero line.
"""
            ),
            **kwargs
        )
