def script_function(i,num):
    script = '''
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
            row.label = label;
            json_data.push(row);
        }
        for(i = 15; i < 35; i++)
        {
            j = 1
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
            row.label = label;
            json_data.push(row);
        }
        exportRaw(json_data, 'cdk.json');
    '''

    script1 = '''
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
    for(i = 0; i < 20; i++)
    {
        var j =1;
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
        row.label = label;
        json_data.push(row);
    }
    exportRaw(json_data, 'cdk.json');
    '''
    if(i==0):
        return script
    else:
        return script1
