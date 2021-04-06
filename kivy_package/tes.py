import requests
res = (requests.get('https://scone-pa.clients6.google.com/static/proxy.html?usegapi=1&jsh=m%3B%2F_%2Fscs%2Fabc-static%2F_%2Fjs%2Fk%3Dgapi.gapi.en.RrjSsKk8Szw.O%2Fd%3D1%2Fct%3Dzgms%2Frs%3DAHpOoo8bhQb3qTfNhmC8kzOOB-dQGGlNzA%2Fm%3D__features__#parent=https%3A%2F%2Fcloud.google.com&rpctoken=637814562')
       )
print(res.text)