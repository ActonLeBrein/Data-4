  var width = 960,
      height = 500,
      outerRadius = Math.min(width, height) * .5 - 10,
      innerRadius = outerRadius * .6;

  var n = 30,
      data0 = d3.range(n).map(Math.random),
      data1 = d3.range(n).map(Math.random),
      data;

  var color = d3.scale.ordinal()
              .domain([0,1,2,3,4,5,6,7,8,9])
              .range(['#181818','#202020','#282828','#303030','#383838','#404040','#484848','#505050','#585858','#606060','#686868'])

  var arc = d3.svg.arc();

  var pie = d3.layout.pie()
      .sort(null);

  var margin = {
      top: 40,
      right: 40,
      bottom: 40,
      left: 40
    }, width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

  var y = d3.scale.ordinal().domain(d3.range(1)).rangePoints([0, height]);

  var svg = d3.select("body #welcome").append("svg")
      .attr("width", width)
      .attr("height", 600);

  var arcss = svg.append("g")
                 .attr("transform", "translate(38.5,40.5)");

  arcss.selectAll(".arc")
      .data(arcs(data0, data1))
    .enter().append("g")
      .attr("class", "arc")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
    .append("path")
      .attr("fill", function(d, i) { return color(i); })
      .attr("d", arc);

  svg.append("svg:image")
      .attr('x',-80)
      .attr('y',100)
      .attr('width', 1122)
      .attr('height', 450)
      .attr("xlink:href","/static/img/main_D4_2.png");

  svg.append("svg:image")
      .attr('x',-93)
      .attr('y',-16)
      .attr('width', 1122)
      .attr('height', 535)
      .attr("xlink:href","/static/img/main_D4_3.png");

  svg.append("svg:image")
      .attr('x',-87)
      .attr('y',102.5)
      .attr('width', 1122)
      .attr('height', 273)
      .attr("xlink:href","/static/img/main_D4_1.png");

  var circulos = svg.append("g");

  circulos.selectAll("circle").data([{'id':'c0','cx':750,'cy':50},
                                     {'id':'c1','cx':800,'cy':150},
                                     {'id':'c2','cx':765,'cy':215},
                                     {'id':'c3','cx':700,'cy':425},
                                     {'id':'c4','cx':300,'cy':500},
                                     {'id':'c5','cx':210,'cy':340},
                                     {'id':'c6','cx':433,'cy':530},
                                     {'id':'c7','cx':300,'cy':40}])
          .enter()
          .append("circle")
          .attr("id", function(d) { return d.id })
          .attr("stroke-width", 10)
          .attr("r", 10)
          .attr("cx", function(d) { return d.cx })
          .attr("cy", function(d) { return d.cy })
          .each(pulse);

  transition(1);

  function arcs(data0, data1) {
    var arcs0 = pie(data0),
        arcs1 = pie(data1),
        i = -1,
        arc;
    while (++i < n) {
      arc = arcs0[i];
      arc.innerRadius = innerRadius;
      arc.outerRadius = outerRadius;
      arc.next = arcs1[i];
    }
    return arcs0;
  }

  function transition(state) {
    var path = d3.selectAll(".arc > path")
        .data(state ? arcs(data0, data1) : arcs(data1, data0));

    // Wedges split into two rings.
    var t0 = path.transition()
        .duration(1000)
        .attrTween("d", tweenArc(function(d, i) {
          return {
            innerRadius: i & 1 ? innerRadius : (innerRadius + outerRadius) / 2,
            outerRadius: i & 1 ? (innerRadius + outerRadius) / 2 : outerRadius
          };
        }));

    // Wedges translate to be centered on their final position.
    var t1 = t0.transition()
        .attrTween("d", tweenArc(function(d, i) {
          var a0 = d.next.startAngle + d.next.endAngle,
              a1 = d.startAngle - d.endAngle;
          return {
            startAngle: (a0 + a1) / 2,
            endAngle: (a0 - a1) / 2
          };
        }));

    // Wedges then update their values, changing size.
    var t2 = t1.transition()
          .attrTween("d", tweenArc(function(d, i) {
            return {
              startAngle: d.next.startAngle,
              endAngle: d.next.endAngle
            };
          }));

    // Wedges reunite into a single ring.
    var t3 = t2.transition()
        .attrTween("d", tweenArc(function(d, i) {
          return {
            innerRadius: innerRadius,
            outerRadius: outerRadius
          };
        }));

    setTimeout(function() { transition(!state); }, 5000);
  }

  function tweenArc(b) {
    return function(a, i) {
      var d = b.call(this, a, i), i = d3.interpolate(a, d);
      for (var k in d) a[k] = d[k]; // update data
      return function(t) { return arc(i(t));
      };
    };
  }

  function pulse() {
      var circle = svg.select("#c" + (Math.floor(Math.random() * ((svg.selectAll("circle")[0]).length))));
      (function repeat() {
        circle = circle.transition()
                 .duration(2000)
                 .attr("stroke-width", Math.random()*20)
                 .attr("r", Math.random(500)*5)
                 .transition()
                 .duration(2000)
                 .attr("stroke-width", Math.random()*10)
                 .attr("r", Math.random(300)*10)
                 .transition()
                 .duration(2000)
                 .attr("stroke-width", Math.random()*15)
                 .attr("r", Math.random(250)*15)
                 .transition()
                 .duration(2000)
                 .attr('stroke-width', Math.random()*1.5)
                 .attr("r", Math.random(200)*25)
                 .ease('sine')
                 .each("end", repeat);
      })
    ();
  }