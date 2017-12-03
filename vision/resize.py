import cv2

files

for each file in files:
    file=filename
    img=cv2.imread(file,1)
    resized_image=cv2.resize(img,(100,100)))
    cv2.imshow("resized", resized_image)
    file_resized=file+"resized.jpg"
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite(file"Galaxy_resized.jpg", resized_image)
