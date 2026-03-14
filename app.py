import cv2 

image = cv2.imread("D:/Python/Opencv/mini project/butterfly.png")

# cv2.imshow("Image is showing" , image)
# cv2.waitKey()
# cv2.destroyAllWindows()

if image is not None :
    print(" Press 1 to Convert to GrayScale----> \n Press 2 to Resize image----> \n Press 3 to Crop Image---> \n Press 4 to Flip Image---> \n Press 5 to Rotate Image-----> \n Press 6 to Save Image---->")
    operation = input("Choose your Operation  : ")
    if operation == "1":
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow("GrayScale image is showing" , gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif operation == "2":
        w = int(input("Enter your desired width : "))
        h = int(input("Enter your desired height : "))
        resized = cv2.resize(image,(w,h) )
        cv2.imshow("Showing your resized image " , resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

else:
    print("Invalid image path check and retry !!!")