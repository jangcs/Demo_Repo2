import dvc.api

resource_url = dvc.api.get_url('m1.pth', repo='git@github.com:jangcs/Demo_Repo2.git', rev="v4.0")
print(resource_url)

modelpth=dvc.api.read('m1.pth', repo='git@github.com:jangcs/Demo_Repo2.git', rev='v4.0', mode='rb')

f=open("m1_pulled.pth","wb")
f.write(modelpth)
f.close()

