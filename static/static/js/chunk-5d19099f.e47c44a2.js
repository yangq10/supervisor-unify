(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5d19099f"],{6114:function(t,e,n){},7424:function(t,e,n){var a="";t.exports={API_PROXY_PREFIX:"".concat(a),LOGIN:"".concat(a,"/login"),ROUTES:"".concat(a,"/routes"),GOODS:"".concat(a,"/goods"),GOODS_COLUMNS:"".concat(a,"/columns")}},"9b97":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("a-spin",{attrs:{spinning:t.spinning,size:"large"}},[n("a-card",{staticStyle:{width:"100%"},attrs:{"tab-list":t.tabList,"active-tab-key":t.key},on:{tabChange:function(e){return t.onTabChange(e,"key")}}},[n("a-collapse",{model:{value:t.activeKey,callback:function(e){t.activeKey=e},expression:"activeKey"}},t._l(t.groupTab,(function(e){return n("a-collapse-panel",{key:e.name,attrs:{header:e.name}},[n("template",{slot:"extra"},[n("a-dropdown",{on:{click:function(t){return t.preventDefault()}}},[n("a",{staticClass:"ant-dropdown-link"},[n("a-icon",{attrs:{type:"setting"},on:{click:t.handleClick}})],1),n("a-menu",{attrs:{slot:"overlay"},slot:"overlay"},[n("a-menu-item",[n("a",{on:{click:function(e){return t.restartGroup()}}},[t._v("重启")])])],1)],1)],1),n("a-table",{attrs:{rowKey:"pid",columns:t.columns,"data-source":e.program_list,size:"small",pagination:!1},scopedSlots:t._u([{key:"tags",fn:function(e,a){return n("span",{},[n("a-tag",{attrs:{color:10===a.state||20===a.state?"#87d068":"#f50"}},[t._v(" "+t._s(e)+" ")])],1)}},{key:"group",fn:function(e){return n("span",{},t._l(e,(function(e,a){return n("a-tag",{key:a,attrs:{color:"#108ee9"}},[t._v(" "+t._s(e)+" ")])})),1)}},{key:"server",fn:function(e){return n("span",{},[n("a-tag",{attrs:{color:"#108ee9"}},[t._v(" "+t._s(e)+" ")])],1)}},{key:"action",fn:function(e,a){return n("span",{staticClass:"a-button"},[n("a",{on:{click:function(e){return t.startServer(a)}}},[t._v("Start")]),n("a-divider",{attrs:{type:"vertical"}}),n("a",{on:{click:function(e){return t.stopServer(a)}}},[t._v("Stop")]),n("a-divider",{attrs:{type:"vertical"}}),n("a",{on:{click:function(e){return t.restartServer(a)}}},[t._v("Restart")]),n("a-divider",{attrs:{type:"vertical"}}),n("a",{on:{click:function(e){return t.openLog(a,"out")}}},[t._v("Tail -f Stdout")]),n("a-divider",{attrs:{type:"vertical"}}),n("a",{on:{click:function(e){return t.openLog(a,"err")}}},[t._v("Tail -f Stderr")]),"hostList"==t.key?[n("a-divider",{attrs:{type:"vertical"}}),n("a-dropdown",{attrs:{trigger:["click"]}},[n("a",{staticClass:"ant-dropdown-link",on:{click:function(t){return t.preventDefault()}}},[t._v(" addGroup "),n("a-icon",{attrs:{type:"down"}})],1),n("a-menu",{attrs:{slot:"overlay"},slot:"overlay"},t._l(t.addGroupList,(function(e,a){return n("a-menu-item",{key:a},[n("a",[t._v(t._s(e.name))])])})),1)],1)]:t._e()],2)}}],null,!0)})],2)})),1),n("template",{slot:"tabBarExtraContent"},[n("a-dropdown",[n("a",{staticClass:"ant-dropdown-link",on:{click:function(t){return t.preventDefault()}}},[t._v(" Timed Refresh "),t.time?[t._v(" ("+t._s(t.time>=60?t.time/60+"min":t.time+"s")+") ")]:t._e(),n("a-icon",{attrs:{type:"down"}})],2),n("a-menu",{attrs:{slot:"overlay"},slot:"overlay"},[n("a-menu-item",[n("a",{on:{click:function(e){return t.setTiming(30)}}},[t._v("30s")])]),n("a-menu-item",[n("a",{on:{click:function(e){return t.setTiming(60)}}},[t._v("1min")])]),n("a-menu-item",[n("a",{on:{click:function(e){return t.setTiming(300)}}},[t._v("5min")])]),n("a-menu-divider"),n("a-menu-item",[n("a",{on:{click:function(e){return t.setTiming("")}}},[t._v("not refresh")])])],1)],1)],1)],2)],1)],1)},r=[],i=(n("b0c0"),n("7424")),o=n("b775");function s(){return Object(o["d"])("".concat(i["API_PROXY_PREFIX"],"/server/list"),o["a"].GET,{})}function c(){return Object(o["d"])("".concat(i["API_PROXY_PREFIX"],"/group/list"),o["a"].GET,{})}function u(t,e){return Object(o["d"])("".concat(i["API_PROXY_PREFIX"],"/program/start"),o["a"].GET,{server:t,program:e})}function d(t,e){return Object(o["d"])("".concat(i["API_PROXY_PREFIX"],"/program/stop"),o["a"].GET,{server:t,program:e})}function l(t,e){return Object(o["d"])("".concat(i["API_PROXY_PREFIX"],"/program/restart"),o["a"].GET,{server:t,program:e})}var m=[{title:"State",key:"statename",dataIndex:"statename",scopedSlots:{customRender:"tags"},width:"10%"},{title:"Name",dataIndex:"name",width:"20%"},{title:"Description",dataIndex:"description",width:"30%"},{title:"Group",dataIndex:"group",scopedSlots:{customRender:"group"},width:"10%"},{title:"Action",dataIndex:"action",scopedSlots:{customRender:"action"}}],p=[{title:"State",key:"statename",dataIndex:"statename",scopedSlots:{customRender:"tags"},width:"10%"},{title:"Name",dataIndex:"name",width:"20%"},{title:"Description",dataIndex:"description",width:"30%"},{title:"Host",dataIndex:"server",scopedSlots:{customRender:"server"},width:"10%"},{title:"Action",dataIndex:"action",scopedSlots:{customRender:"action"}}],v={name:"supervisorList",data:function(){return{spinning:!1,tabList:[{key:"hostList",tab:"HostList"},{key:"groupList",tab:"GroupList"}],key:"hostList",activeKey:[],columns:m,groupTab:[],addGroupList:[],timer:"",time:""}},watch:{key:function(t){this.columns="groupList"===t?p:m}},created:function(){this.time=localStorage.getItem("supervisorTime"),this.time&&this.setTiming(this.time),this.initData()},methods:{onTabChange:function(t,e){this[e]=t,this.initData()},handleClick:function(t){t.stopPropagation()},initData:function(){var t=this;t.activeKey=[],"hostList"===t.key?s().then((function(e){if(0===e.data.code){var n=e.data.info;t.groupTab=n;for(var a=0;a<n.length;a++)t.activeKey.push(n[a].name)}else t.$message.error(e.data.msg)})):"groupList"===t.key?c().then((function(e){if(0===e.data.code){for(var n=e.data.info,a=0;a<n.length;a++)t.activeKey.push(n[a].name),t.addGroupList=n;t.groupTab=n}else t.$message.error(e.data.msg)})):t.$message.error("未知错误")},setTiming:function(t){var e=this;e.time=t,clearInterval(e.timer),""===t?localStorage.removeItem("supervisorTime"):(localStorage.setItem("supervisorTime",t),e.timer=setInterval((function(){e.initData()}),1e3*t))},restartGroup:function(){},startServer:function(t){var e=this;e.spinning=!0,u(t.server,t.name).then((function(t){0===t.data.code?(e.$message.success(t.data.msg),e.initData(),e.spinning=!1):(e.$message.error(t.data.msg),e.spinning=!1)}))},stopServer:function(t){var e=this;e.spinning=!0,d(t.server,t.name).then((function(t){0===t.data.code?(e.$message.success(t.data.msg),e.initData(),e.spinning=!1):(e.$message.error(t.data.msg),e.spinning=!1)}))},restartServer:function(t){var e=this;e.spinning=!0,l(t.server,t.name).then((function(t){0===t.data.code?(e.$message.success(t.data.msg),e.initData(),e.spinning=!1):(e.$message.error(t.data.msg),e.spinning=!1)}))},openLog:function(t,e){this.$openPage("/log?server="+t.server+"&name="+t.name+"&type="+e)}}},g=v,f=(n("a000"),n("0c7c")),h=Object(f["a"])(g,a,r,!1,null,"fa32e83c",null);e["default"]=h.exports},a000:function(t,e,n){"use strict";var a=n("6114"),r=n.n(a);r.a}}]);