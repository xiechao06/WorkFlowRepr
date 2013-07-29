function Colors(dictonary) {
    function sort(dict){
        var values = $.map(dict, function(value, key){return value});
        return values.sort();
    }
    this.array = sort(dictonary);

    this.get = function (idx, total_size, default_value) {
        idx = Math.round((idx + 1) * this.array.length / (total_size + 1));
        return this.array[idx] ? this.array[idx] : (default_value ? default_value : undefined);
    }
}

COLORS = new Colors({"AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF",
    "BlueViolet": "#8A2BE2",
    "Brown": "#A52A2A",
    "BurlyWood": "#DEB887",
    "CadetBlue": "#5F9EA0",
    "Chartreuse": "#7FFF00",
    "Chocolate": "#D2691E",
    "Coral": "#FF7F50",
    "CornflowerBlue": "#6495ED",
    "Cornsilk": "#FFF8DC",
    "Crimson": "#DC143C",
    "Cyan": "#00FFFF",
    "DarkBlue": "#00008B",
    "DarkCyan": "#008B8B",
    "DarkGoldenRod": "#B8860B",
    "DarkGray": "#A9A9A9",
    "DarkGreen": "#006400",
    "DarkKhaki": "#BDB76B",
    "DarkMagenta": "#8B008B",
    "DarkOliveGreen": "#556B2F",
    "DarkOrange": "#FF8C00",
    "DarkOrchid": "#9932CC",
    "DarkRed": "#8B0000",
    "DarkSalmon": "#E9967A",
    "DarkSeaGreen": "#8FBC8F",
    "DarkSlateBlue": "#483D8B",
    "DarkSlateGray": "#2F4F4F",
    "DarkTurquoise": "#00CED1",
    "DarkViolet": "#9400D3",
    "DeepPink": "#FF1493",
    "DeepSkyBlue": "#00BFFF",
    "DimGray": "#696969",
    "DodgerBlue": "#1E90FF",
    "FireBrick": "#B22222",
    "FloralWhite": "#FFFAF0",
    "ForestGreen": "#228B22",
    "Fuchsia": "#FF00FF",
    "Gainsboro": "#DCDCDC",
    "GhostWhite": "#F8F8FF",
    "Gold": "#FFD700",
    "GoldenRod": "#DAA520",
    "Gray": "#808080",
    "Green": "#008000",
    "GreenYellow": "#ADFF2F",
    "HoneyDew": "#F0FFF0",
    "HotPink": "#FF69B4",
    "IndianRed": "#CD5C5C",
    "Indigo": "#4B0082",
    "Ivory": "#FFFFF0",
    "Khaki": "#F0E68C",
    "Lavender": "#E6E6FA",
    "LavenderBlush": "#FFF0F5",
    "LawnGreen": "#7CFC00",
    "LemonChiffon": "#FFFACD",
    "LightBlue": "#ADD8E6",
    "LightCoral": "#F08080",
    "LightCyan": "#E0FFFF",
    "LightGoldenRodYellow": "#FAFAD2",
    "LightGray": "#D3D3D3",
    "LightGreen": "#90EE90",
    "LightPink": "#FFB6C1",
    "LightSalmon": "#FFA07A",
    "LightSeaGreen": "#20B2AA",
    "LightSkyBlue": "#87CEFA",
    "LightSlateGray": "#778899",
    "LightSteelBlue": "#B0C4DE",
    "LightYellow": "#FFFFE0",
    "Lime": "#00FF00",
    "LimeGreen": "#32CD32",
    "Linen": "#FAF0E6",
    "Magenta": "#FF00FF",
    "Maroon": "#800000",
    "MediumAquaMarine": "#66CDAA",
    "MediumBlue": "#0000CD",
    "MediumOrchid": "#BA55D3",
    "MediumPurple": "#9370DB",
    "MediumSeaGreen": "#3CB371",
    "MediumSlateBlue": "#7B68EE",
    "MediumSpringGreen": "#00FA9A",
    "MediumTurquoise": "#48D1CC",
    "MediumVioletRed": "#C71585",
    "MidnightBlue": "#191970",
    "MintCream": "#F5FFFA",
    "MistyRose": "#FFE4E1",
    "Moccasin": "#FFE4B5",
    "NavajoWhite": "#FFDEAD",
    "Navy": "#000080",
    "OldLace": "#FDF5E6",
    "Olive": "#808000",
    "OliveDrab": "#6B8E23",
    "Orange": "#FFA500",
    "OrangeRed": "#FF4500",
    "Orchid": "#DA70D6",
    "PaleGoldenRod": "#EEE8AA",
    "PaleGreen": "#98FB98",
    "PaleTurquoise": "#AFEEEE",
    "PaleVioletRed": "#DB7093",
    "PapayaWhip": "#FFEFD5",
    "PeachPuff": "#FFDAB9",
    "Peru": "#CD853F",
    "Pink": "#FFC0CB",
    "Plum": "#DDA0DD",
    "PowderBlue": "#B0E0E6",
    "Purple": "#800080",
    "RosyBrown": "#BC8F8F",
    "RoyalBlue": "#4169E1",
    "SaddleBrown": "#8B4513",
    "Salmon": "#FA8072",
    "SandyBrown": "#F4A460",
    "SeaGreen": "#2E8B57",
    "SeaShell": "#FFF5EE",
    "Sienna": "#A0522D",
    "Silver": "#C0C0C0",
    "SkyBlue": "#87CEEB",
    "SlateBlue": "#6A5ACD",
    "SlateGray": "#708090",
    "Snow": "#FFFAFA",
    "SpringGreen": "#00FF7F",
    "SteelBlue": "#4682B4",
    "Tan": "#D2B48C",
    "Teal": "#008080",
    "Thistle": "#D8BFD8",
    "Tomato": "#FF6347",
    "Turquoise": "#40E0D0",
    "Violet": "#EE82EE",
    "Wheat": "#F5DEB3",
    "WhiteSmoke": "#F5F5F5",
    "Yellow": "#FFFF00",
    "YellowGreen": "#9ACD32"
});

var WorkFlowRepr = function (canvas, tree, compress_range, width, height) {
    this.canvas = canvas;
    this.tree = tree;
    this.width = width? width: 960;
    this.height = height? height: 640;
    this.compress_range = compress_range;
    $(canvas).prepend('<input type="checkbox" checked id="display-event-description" />是否展示事件描述');
}


WorkFlowRepr.prototype.margin = 60;
WorkFlowRepr.prototype.lifeCycleLineWidth = 5;

function _getNodeCount(tree) {
    if (!tree) {
        return 0;
    }
    var ret = 1;
    for (group in tree.childrenGroups) {
        for (children in group.items()) {
            ret += _getNodeCount(children);
        }
    }
    return ret;
}

function get_attr(list, attrName, encode) {
    var result = "";
    $.each(list, function (idx, value) {
        temp = value[attrName];
        if (!temp){
            return true;
        }
        if (list.length > 1) {
            if (encode) {
                temp = "&lt;" + temp +"&gt;";
            }else{
                temp = "<" + temp + ">";
            }
        }
        result += temp;
        if (idx < list.length - 1) {
            result += ","
        }
    });
    return result;
}

_traversTree = function(tree) {
    var ret = [];
    function _doTraverseTree(subTree, list) {
        if (!subTree) {
            return;
        }
        list.push(subTree);
        if (subTree.hasOwnProperty('childrenGroups')) {
            for (var i=0; i < subTree.childrenGroups.length; ++i) {
                var group = subTree.childrenGroups[i];
                for (var j=0; j < group.items.length; ++j) {
                    var children = group.items[j];
                    children.parent_ = subTree;
                    _doTraverseTree(children, list)
                }
            }
        }
    };
    _doTraverseTree(tree, ret);
    return ret;
};

WorkFlowRepr.prototype.getMaxPeriod = function () {
    var nodes = _traversTree(this.tree);
    var max = 0;
    $.each(nodes, function(idx, node){
        max = Math.max(max, new Date(node.events[node.events.length - 1].datetime).getTime() - new Date(node.events[0].datetime).getTime());
    });
    return max
}


WorkFlowRepr.prototype.draw = function () {
    var nodes = _traversTree(this.tree);
    var steps = (this.height - 2 * this.margin) / nodes.length;
    var drawableWidth = this.width - 2 * this.margin;

    var draw = SVG(this.canvas).size(this.width, this.height);
    // draw the swim lane
    var firstNode = nodes[0];
    var beginTime = new Date(firstNode.events[0].datetime);
    var endTime = new Date("1970-01-01T00:00:00");
    var max = this.getMaxPeriod();
    for (var i=0; i < nodes.length; ++i) {
        var node = nodes[i];
        node.idx = i;
        var x = this.margin;
        var y = this.margin + i * steps;
        for (var j=x; j < x + drawableWidth; j += 10) {
            draw.line(j, y, j + 5, y).stroke({width: 1, color: 'grey'});
        }
        
        var text = draw.text(node.name).move(x, y - 30).font({
            size: 20,
            anchor: 'top',
        }).attr({
            'data-ot': node.description,
            'data-role': 'node-name'
        }).fill({color: 'gray'});
        text.click((function (target) {
            return function () {
                window.open(target); 
            }
        })(node.target));
        var node_begin_time = new Date(node.events[0].datetime);
        var node_end_time = new Date(node.events[node.events.length-1].datetime); 
        if (node_begin_time < beginTime) {
            beginTime = node_begin_time;
        }
        if (node_end_time > endTime) {
            endTime = node_end_time;
        }
    }
    var timespan = endTime.getTime() - beginTime.getTime();


    function _calcEventPos(event_) {
        return drawableWidth * (new Date(event_.datetime).getTime() - beginTime.getTime()) / timespan;
    }

    var lifeCycleLayer = [];

    var eventDiameter = 10;
    for (var i=0; i < nodes.length; ++i) {
        var node = nodes[i], group_size = [], lastDate = "";
        var color = COLORS.get(i, nodes.length);
        for (var j=0; j < node.events.length; ++j) {
            var event_ = node.events[j];
            group_size.push(event_);

            var eventPoint = [this.margin + _calcEventPos(event_), this.margin + i * steps];
            if (j==0) {
                var start = eventPoint;
            }
            if (j < node.events.length - 1 && new Date(node.events[j + 1].datetime).getTime() - new Date(event_.datetime).getTime() < max * this.compress_range / 100) {
                continue;
            } else {
                if (group_size.length > 1) {
                    var avg = (_calcEventPos(group_size[0]) + _calcEventPos(group_size[group_size.length - 1])) / 2
                    eventPoint = [this.margin + avg, this.margin + i * steps];
                    var circle = draw.ellipse(eventDiameter * group_size.length, eventDiameter).center(eventPoint[0], eventPoint[1])
                } else {
                    circle = draw.circle(eventDiameter).center(eventPoint[0], eventPoint[1])
                }
                circle.fill({color: "green"}).attr(
                        {
                            'data-actor': get_attr(group_size, "actor"),
                            'data-datetime': get_attr(group_size, "datetime"),
                            'data-name': get_attr(group_size, "name"),
                            'data-placement': 'bottom',
                            'data-trigger': 'hover',
                            'data-ot': get_attr(group_size, "description", true)
                        }
                    );
                circle.mouseover((function (eventPoint) {
                return function (event) {
                    this.scale(2, 2).center(eventPoint[0], eventPoint[1]);
                    this.fill({color: 'red'});
                }
            })(eventPoint));
            circle.mouseleave((function (eventPoint) {
                return function (event) {
                    this.scale(1, 1).center(eventPoint[0], eventPoint[1]).fill({color: 'green'});
                }
            })(eventPoint))
            var textPoint = [eventPoint[0], eventPoint[1] + 5];
            if (j & 1) {
                textPoint[1] -= 40;
            }
            function pad(n){
                return n<10 ? '0'+n : n
            }
            var dateString ="", name="";
            var d = new Date(group_size[0].datetime);
            if (!(lastDate && lastDate.year == d.getUTCFullYear() && lastDate.month == d.getUTCMonth() && lastDate.day == d.getUTCDate())) {
                dateString += pad(d.getUTCMonth() + 1) + '-' + pad(d.getUTCDate()) + ' ';
            }
            lastDate = {
                year: d.getUTCFullYear(),
                month: d.getUTCMonth(),
                day: d.getUTCDate()
            };
            dateString += pad(d.getUTCHours()) + ':' + pad(d.getUTCMinutes());
            if (group_size.length > 1){
                var d = new Date(group_size[group_size.length-1].datetime);
                dateString += "~";
                if (!(lastDate && lastDate.year == d.getUTCFullYear() && lastDate.month == d.getUTCMonth() && lastDate.day == d.getUTCDate())) {
                    dateString += pad(d.getUTCMonth() + 1) + '-' + pad(d.getUTCDate()) + ' ';
                }
                lastDate = {
                    year: d.getUTCFullYear(),
                    month: d.getUTCMonth(),
                    day: d.getUTCDate()
                };
                dateString += pad(d.getUTCHours()) + ':' + pad(d.getUTCMinutes());
            }
            draw.text(get_attr(group_size,"name")+"\n"+dateString).move(textPoint[0], textPoint[1]).font({
                size: 10,
                anchor: 'middle'
            }).attr({
                'data-role': 'event-name'
            });
                group_size = [];
            }
        }
        var line = draw.line(start[0], start[1], eventPoint[0], eventPoint[1]).stroke({color: color, width: this.lifeCycleLineWidth}).attr({
            'data-role': 'life-cycle',
            'data-ot': node.description,
        });
        line.mouseover((function (line_width) {
            return function (event) {
            this.stroke({width: line_width * 2});
            }
        })(this.lifeCycleLineWidth));
        line.mouseleave((function (line_width) {
            return function (event) {
            this.stroke({width: line_width});
            }
        })(this.lifeCycleLineWidth));
        lifeCycleLayer.push(line); 
        // draw branches
        var childCnt = 0;
        var lastChildCreateTime = new Date();
        for (var j=0; j < node.childrenGroups.length; ++j) {
            var group = node.childrenGroups[j];
            for (var k=0; k < group['items'].length; ++k) {
                var childNode = group['items'][k];
                if (childNode.events[0].datetime != lastChildCreateTime) {
                    childCnt = 0;
                    lastChildCreateTime = childNode.events[0].datetime;
                } 
                var y1 = this.margin + childNode.idx * steps;
                var y2 = this.margin + node.idx * steps;
                var x1 = x2 = this.margin + _calcEventPos(childNode.events[0]);
                var path = 'M' + x2 + ',' + y2 + ' ';
                path += 'A' + (childCnt * 25) + ',' + (y1 - y2)/2 + ' ';
                path += '0 ';
                path += '0,0 ';
                path += x1 + ',' + (y1 - eventDiameter);
                draw.path(path, true).stroke({width: 1, color: color}).fill('none').attr('marker-end', 'url(#Triangle)');
                ++childCnt;
            }
        }
    }
    for (var i=0; i < lifeCycleLayer.length; ++i) {
        lifeCycleLayer[i].back();
    }
    $('text[data-role="node-name"], line[data-role="life-cycle"], ellipse').each(function () {
        if ($(this).attr('data-ot')) {
            new Opentip($(this), $(this).attr('data-ot'));
        }
   });
      $("#display-event-description").change(function () {
        if (this.checked)  {
          $('text[data-role="event-name"]').show();
        } else {
          $('text[data-role="event-name"]').hide();
        }
      });

    var svgNode = document.getElementsByTagName('svg')[0];
    var defs = svgNode.getElementsByTagName('defs')[0];
    var marker = document.createElementNS('http://www.w3.org/2000/svg', 'marker');
    marker.setAttribute('id', 'Triangle');
    marker.setAttribute('refX', '5');
    marker.setAttribute('refY', '5');
    marker.setAttribute('markerWidth', '14');
    marker.setAttribute('markerHeight', '13');
    marker.setAttribute('orient', 'auto');
    var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    marker.appendChild(path);
    path.setAttribute('d', 'M 0 0 L 10 5 L 0 10 z');
    svgNode.appendChild(defs);
    defs.appendChild(marker);
}
