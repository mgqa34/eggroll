import{d as c,v as p,_ as m,b as _,o as v,s as f,w as i,e as t,t as s}from"./index-b74be412.js";const C=c({name:"clusterCard",componentName:"clusterCard",props:{item:{type:Object},detail:{type:Boolean,default:!0}},setup(e){function n(d){e.detail&&p.push(`/processor?id=${d.serverNodeId}`)}return{toDetail:n}}});const b={class:"cluster-title"},N={class:"cluster-detail"};function $(e,n,d,h,y,S){const u=_("el-card");return v(),f(u,{class:"cluster-card",onClick:n[0]||(n[0]=a=>e.toDetail(e.item))},{header:i(()=>{var a,o,r,l;return[t("div",b,[t("span",null,"IP: "+s((a=e.item)==null?void 0:a.host)+":"+s((o=e.item)==null?void 0:o.port),1),t("span",null,"Name: "+s((r=e.item)!=null&&r.name?(l=e.item)==null?void 0:l.name:"-"),1)])]}),default:i(()=>{var a,o,r,l;return[t("div",N,[t("div",null,"Resources Status: "+s((a=e.item)==null?void 0:a.nodeResourceStatus),1),t("div",null,"Node Status: "+s((o=e.item)==null?void 0:o.serverNodeStatus),1),t("div",null,"allocated: "+s((r=e.item)==null?void 0:r.allocated),1),t("div",null,"total: "+s((l=e.item)==null?void 0:l.total),1)])]}),_:1})}const k=m(C,[["render",$],["__scopeId","data-v-e53b901b"]]);export{k as c};
