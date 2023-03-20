/*
v1.0（后续文本处理较难）
*/

//下载函数
var exportRaw = function(data,name) {
    let urlObject = window.URL || window.webkitURL || window;
    let export_blob = new Blob([data]);
    let save_link = document.createElementNS("http://www.w3.org/1999/xhtml", "a")
    save_link.href = urlObject.createObjectURL(export_blob);
    save_link.download = name;
    save_link.click();
}
//捕获定位
var a = window.frames['contentFrame'].document.getElementById("comment-box").getElementsByClassName("cmmts j-flag")
let data = a[0].innerText
exportRaw(data, 'cdk.txt')

/*
v1.1
该版本主要针对爬取格式修改
用txt格式输出较难处理，本次修改为json格式输出
同时需要对下载函数进行修改
*/
var exportRaw = function(data,name) {
    let jsonstr = (data instanceof Object) ? JSON.stringify(data) : data;
    let urlObject = window.URL || window.webkitURL || window;
    let export_blob = new Blob([jsonstr]);
    let save_link = document.createElementNS("http://www.w3.org/1999/xhtml", "a");
    save_link.href = urlObject.createObjectURL(export_blob);
    save_link.download = name;
    save_link.click();
}
var a = window.frames['contentFrame'].document.getElementById("comment-box").getElementsByClassName("itm");
json_data = [];
for(i = 0; i < 15; i++)
{
    userName = a[i].children[1].children[0].children[0].children[0].innerText;
    content_data = a[i].children[1].children[0].children[0].innerText;
    datetime = a[i].children[1].children[1].children[0].innerText;
    var label = "精选评论"
    row = {};
    row.user = userName;
    row.content = content_data;
    row.time = datetime;
    json_data.push(row);
}
for(i = 15; i < 35; i++)
{
    var j = 1;
    if (a[i].children[1].childElementCount == 3){
        j = 2;
    }
    userName = a[i].children[1].children[0].children[0].children[0].innerText;
    content_data = a[i].children[1].children[0].children[0].innerText;
    datetime = a[i].children[1].children[j].children[0].innerText;
    var label = "最新评论"
    row = {};
    row.user = userName;
    row.content = content_data;
    row.time = datetime;
    json_data.push(row);
}
exportRaw(json_data, 'cdk.json');
