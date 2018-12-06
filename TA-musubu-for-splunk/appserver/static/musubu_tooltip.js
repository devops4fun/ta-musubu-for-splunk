require([
    'underscore',
    'jquery',
    'splunkjs/mvc',
    'splunkjs/mvc/searchmanager',
    'splunkjs/mvc/tableview',
    'splunkjs/mvc/textinputview',
    'splunkjs/mvc/simplexml/ready!'
], function(_, $, mvc, SearchManager, TableView, TextInputView) {

    //define search managers

    // // Search query is based on the selected index
    // var musubu_search_main = new SearchManager({
    //     id: "musubusearchmain",
    //     cache: true,
    //     search: mvc.tokenSafe("$searchQuery$")
    // });

    // new TextInputView({
    //     id: "musubu_textinput_ip",
    //     value: mvc.tokenSafe("$musubu_textinput_ip$"),
    //     default: "Real-time IP lookup (Coming Soon...)",
    //     disabled: false,
    //     el: $("#musubu_textinput_ip")
    // }).render();

    // var musubu_search_2 = new SearchManager({
    //   id: "musubu_search_2",
    //   search: "| inputlookup ip_test_data",
    //   preview: true,
    //   cache: true
    // });
    //
    // //Setup a custom view
    // var musubu_tbl_2 = new TableView({
    //   id: "musubu_tbl_2",
    //   managerid:"musubu_search_2",
    //   pageSize: 5,
    //   wrap: true,
    //   drilldown: "cell",
    //   el: $("#musubu_tbl_2")
    // }).render();

  //   //setup event handlers to customize drilldowns
  //   musubu_tbl_2.on("click", function(e) {
  //   // Bypass the default behavior
  //   e.preventDefault();
  //
  //   $.contextMenu({
  //   selector: '.context-menu-one',
  //   trigger: 'left',
  //   callback: function(key, options) {
  //       var m = "clicked: " + key;
  //       console.log(m);
  //   },
  //   items: {
  //       "edit": {name: "Edit", icon: "edit"},
  //       "cut": {name: "Cut", icon: "cut"},
  //       "copy": {name: "Copy", icon: "copy"},
  //       "paste": {name: "Paste", icon: "paste"},
  //       "delete": {name: "Delete", icon: "delete"},
  //       "sep1": "---------",
  //       "quit": {name: "Quit", icon: function($element, key, item){ return 'context-menu-icon context-menu-icon-quit'; }}
  //       }
  //   });
  //   var musubu_td = document.querySelectorAll("td");
  //   //check for the column row item of ip
  //   console.log(Object.keys(e).forEach(function (key) {
  //     // do something with e[key]
  //     if (key === 'event'){
  //       var rowdata = e[key].rowContext;
  //       Object.keys(rowdata).forEach(function(key){
  //         if(key === 'row.ip'){
  //           //get ip value from clicked event data
  //         rowip = rowdata[key];
  //
  //         // XHR request to the Musbu API
  //         var oReq = new XMLHttpRequest();
  //         var base_url = 'https://api.musubu.io/MusubuAPI/Musubu';
  //         var apikey = '41c91a0c9db56d77dde0089945dfd64b';
  //         var urloptions = 'format=JSON&level=verbose';
  //         var url = base_url + '?' + 'IP=' + rowip + '&' + 'key=' + apikey + '&' + urloptions;
  //         oReq.open("GET", url);
  //         var type = oReq.responseType;
  //         oReq.onreadystatechange = checkData;
  //         oReq.responseType = "json";
  //         oReq.send(null);
  //
  //         function checkData()
  //         {
  //             //api call to musubu api
  //               if (oReq.readyState === oReq.DONE) {
  //                 if (oReq.status === 200) {
  //                   // get response object
  //                   var oRes = oReq.response;
  //                   for (var key in oRes) {
  //                       if (oRes.hasOwnProperty(key)) {
  //                           console.log(key + " : " + oRes[key]);
  //                       }
  //                   }
  //             //diplay context Menu
  //               } //end if
  //             } // end readystate check
  //         }
  //       } //end if
  //     }) //end forEach function
  //   } // end event check conditional
  //   }));
  // }); // end click event handler for musubu table

    var CustomTooltipRenderer = TableView.BaseCellRenderer.extend({
        canRender: function(cell) {
            return cell.field === 'ip';
        },
        render: function($td, cell) {
            var musubu_ip = cell.value;
            // XHR request to the Musbu API
            var oReq = new XMLHttpRequest();
            var base_url = 'https://api.musubu.io/MusubuAPI/Musubu';
            var apikey = 'placeholder';
            var urloptions = 'format=JSON&level=verbose';
            var url = base_url + '?' + 'IP=' + musubu_ip + '&' + 'key=' + apikey + '&' + urloptions;
            oReq.open("GET", url);
            var type = oReq.responseType;
            oReq.onreadystatechange = checkData;
            oReq.responseType = "json";
            oReq.send(null);

            function checkData()
            {
                //api call to musubu api
                  if (oReq.readyState === oReq.DONE) {
                    if (oReq.status === 200) {
                      // get response object; store musubu values in variables
                      var oRes = oReq.response;
                      for (var key in oRes) {
                          if (oRes.hasOwnProperty(key)) {
                            if(key === 'threat_potential_score_pct'){
                              var threat_score = key;
                              var threat_score_value = oRes[key];
                            }  else if(key === 'threat_classification'){
                                var threat_classification = key;
                                var threat_classification_value = oRes[key];
                              }
                              else if(key === 'blacklist_class'){
                                  var blacklist_class = key;
                                  var blacklist_class_value = oRes[key];
                                }
                                else if(key === 'blacklist_class_cnt'){
                                    var blacklist_class_cnt = key;
                                    var blacklist_class_cnt_value = oRes[key];
                                  }
                                  else if(key === 'blacklist_network_neighbor_cnt'){
                                      var blacklist_network_neighbor_cnt = key;
                                      var blacklist_network_neighbor_cnt_value = oRes[key];
                                    }
                                    else if(key === 'blacklist_observations'){
                                        var blacklist_observations = key;
                                        var blacklist_observations_value = oRes[key];
                                      }
                                      else if(key === 'ipaddress'){
                                          var ipaddress = key;
                                          var ipaddress_value = oRes[key];
                                        }
                          }
                      }
                //diplay context Menu
                  } //end if
                } // end readystate check
                var tip_content = "Threat Data for IP: " + ipaddress_value + "\n\n Threat Score: " + threat_score_value + "\n Threat Classification: " + threat_classification_value + "\n Blacklist Class: " + blacklist_class_value + "\n Blacklist Count: " + blacklist_class_cnt_value + "\n Blacklist Network Neighbors: " + blacklist_network_neighbor_cnt_value + "\n Blacklist Observations: " + blacklist_observations_value + "\n";

                //store IP value
                var message = cell.value;
                var tip = tip_content;
                if(message.length > 48) { message = message.substring(0,47) + "..." }

                $td.html(_.template('<a href="#" class="musubu_context_menu_one" data-toggle="tooltip" data-placement="left" title="<%= tip%>"><%- message%></a>', {
                                tip: tip,
                                message: message
                            }));

                // This line wires up the Bootstrap tooltip to the cell markup
                $td.children('[data-toggle="tooltip"]').tooltip();

            }

        }
    });

    mvc.Components.get('musubu_tbl').getVisualization(function(tableView) {

        // Register custom cell renderer
        tableView.table.addCellRenderer(new CustomTooltipRenderer());

        // Force the table to re-render
        tableView.table.render();
    });

});
