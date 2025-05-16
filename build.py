import os

with open("lib_template.html") as input:
    with open("lib.html", "w") as output:
        res = []
        for i in os.listdir("libs"):
            lib, name = i.split(".", 1)
            name, _ = name.rsplit(".", 1)
            res.append(f'<a href="./libs/{i}">{lib}/{name}</a><br>')
        output.write(t:=input.read().replace("<!--STYLE-->", '''
    <style>
        * {
            color: white;
            background-color: #222222;
            word-wrap: break-word;
            word-break: break-word;
            overflow: hide;
        }
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .title {
            background-color: #2C3E50;
            border-radius: 10px;
            padding: 6px;
            padding-left: 5px;
        }
        h1, h2 {
            margin-bottom: 20px;
        }
        pre {
            background-color: #333333;
            border-radius: 10px;
            padding: 6px;
            overflow: scroll;
        }
    </style>''').replace("<!--FILES-->", "\n"+"\n".join(res)+"\n"))