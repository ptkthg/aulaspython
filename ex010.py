medida = float (input("Digite o tamanho do prédio:"))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print ('A médida corresponde em quilometros à {}, \n em hectometros à {} \n em decametros à {} \n em metros à {} \n em decimetros à {} \n em centimentros à {} \nem milimetros à {}'.format(km,dm,hm,medida,dam,cm,mm))
