import cv2 

image = cv2.imread("D:/Python/Opencv/mini project/butterfly.png")
# print(image.shape)

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

    elif operation == "3":
        t = int(input("Enter  top  point : "))
        l = int(input("Enter left point : "))
        b = int(input("Enter bottom  point : "))
        r = int(input("Enter  right point : "))

        croped = image[ t:b , l:r]
        cv2.imshow("Showing your croped image " , croped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif operation == "4":
        choice = input("Enter your choice Horizontal / vertical/ both :").lower()
        def image_flip(c):
            fliped = cv2.flip(image , c)
            cv2.imshow("Showing your fliped image " , fliped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            
        if choice == 'horizontal':
            choice = 1
            image_flip(choice)
        elif choice == 'vertical' :
            choice = 0 
            image_flip(choice)

        elif choice == 'both':
            choice = -1
            image_flip(choice)

        else:
            print("Invalid Choice !!!!!!")

    elif operation == '5':
        h,w = image.shape[:2]
        center = (w//2, h//2)
        angle = int(input("Enter your roatation angle : "))

        M = cv2.getRotationMatrix2D(center, angle , 1.0)
        rotation = cv2.warpAffine(image,M,(w,h))
        cv2.imshow("Showing your Rotated image " , rotation)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



else:
    print("Invalid image path check and retry !!!")