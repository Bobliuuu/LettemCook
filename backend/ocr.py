import easyocr
reader = easyocr.Reader(['en']) 
result = reader.readtext('linear algebra.png', detail = 0)
print(" ".join(result))
