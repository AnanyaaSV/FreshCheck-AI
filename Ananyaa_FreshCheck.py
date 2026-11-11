
import cv2
import numpy as np

print("================================")
print("          FRESHCHECK AI")
print("       FOOD QUALITY CHECKER")
print("================================")

# Step 1: Upload image
image_path = input("\nEnter image file name: ")
image = cv2.imread(image_path)


# Check whether image exists
if image is None:
    print("\nERROR: Image not found!")
    print("Please enter a valid image file path.")

else:
    # Step 2: Resize image
    image = cv2.resize(image, (400, 400))

    # Step 3: Convert image into HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Step 4: Calculate average HSV values
    average = np.mean(hsv, axis=(0, 1))

    hue = average[0]
    saturation = average[1]
    brightness = average[2]

    print("\n========== FOOD REPORT ==========")

    print(f"Average Hue: {hue:.2f}")
    print(f"Average Saturation: {saturation:.2f}")
    print(f"Average Brightness: {brightness:.2f}")

    # Step 5: Food appearance analysis

    if (
        (15 <= hue <= 25 and saturation < 80 and brightness > 230)
        or
        (40 <= hue <= 60 and saturation < 50)
    ):

        result = "SPOILED-LOOKING"

        print("\nRESULT:", result)

        print("\nWHY WAS THIS PREDICTED?")
        print("1. The image matches a low-saturation colour rule.")
        print("2. The average colour values match the selected thresholds.")
        print("3. The appearance may indicate a need for closer inspection.")

        print("\nRECOMMENDATION:")
        print("Please inspect the food carefully.")
        print("Do not consume food that may be spoiled.")

    else:

        result = "FRESH-LOOKING"

        print("\nRESULT:", result)

        print("\nWHY WAS THIS PREDICTED?")
        print("1. The image does not match the selected warning rules.")
        print("2. The average colour values are outside the warning thresholds.")
        print("3. The food appears acceptable based on this basic colour analysis.")

        print("\nRECOMMENDATION:")
        print("Continue with normal food inspection.")
       


    # Step 6: Display final report
    
    cv2.imshow("FreshCheck AI - Food Scanner", image)
    print("\n================================")
    print("       FRESHCHECK SUMMARY")
    print("================================")
    print("Food Appearance:", result)
    print("Average Hue:", round(hue, 2))
    print("Average Saturation:", round(saturation, 2))
    print("Average Brightness:", round(brightness, 2))

    print("\nNOTE:")
    print("This is an experimental image-based colour check.")
    print("It cannot confirm whether food is safe to eat.")

    print("\n================================")
    print("   THANK YOU FOR USING FRESHCHECK")
    print("================================")
    cv2.imshow("FreshCheck AI - Food Scanner", image)


# Step 7: Display image

cv2.namedWindow("FreshCheck AI - Food Scanner", cv2.WINDOW_NORMAL)
cv2.imshow("FreshCheck AI - Food Scanner", image)

# Bring the image window to the front
cv2.setWindowProperty("FreshCheck AI - Food Scanner", cv2.WND_PROP_TOPMOST, 1)

cv2.waitKey(0)
cv2.destroyAllWindows()


