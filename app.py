
import streamlit as st
import cv2
import numpy as np

# FreshCheck AI - Online Application

st.set_page_config(
    page_title="FreshCheck AI",
    page_icon="🥑",
    layout="centered"
)

st.title("🥑 FRESHCHECK AI")
st.subheader("Food Quality Checker")

st.write(
    "Upload an image of a fruit or vegetable "
    "to analyse its appearance."
)

# Step 1: Upload image
uploaded_file = st.file_uploader(
    "Upload Food Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Step 2: Read uploaded image
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        st.error("Image not found or invalid!")

    else:

        # Step 3: Resize image
        image = cv2.resize(image, (400, 400))

        # Display image
        st.image(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
            caption="Uploaded Food Image",
            width=400
        )

        # Step 4: Convert image into HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Step 5: Calculate average HSV values
        average = np.mean(hsv, axis=(0, 1))

        hue = average[0]
        saturation = average[1]
        brightness = average[2]

        st.subheader("FOOD REPORT")

        st.write(f"Average Hue: {hue:.2f}")
        st.write(f"Average Saturation: {saturation:.2f}")
        st.write(f"Average Brightness: {brightness:.2f}")

        # Step 6: Food appearance analysis

        if (
            (15 <= hue <= 25 and saturation < 80 and brightness > 230)
            or
            (40 <= hue <= 60 and saturation < 50)
        ):

            result = "SPOILED-LOOKING"

            st.error("RESULT: " + result)

            st.subheader("WHY WAS THIS PREDICTED?")

            st.write("1. The image matches a low-saturation colour rule.")
            st.write("2. The average colour values match the selected thresholds.")
            st.write("3. The appearance may indicate a need for closer inspection.")

            st.subheader("RECOMMENDATION")

            st.write("Please inspect the food carefully.")
            st.write("Do not consume food that may be spoiled.")

        else:

            result = "FRESH-LOOKING"

            st.success("RESULT: " + result)

            st.subheader("WHY WAS THIS PREDICTED?")

            st.write("1. The image does not match the selected warning rules.")
            st.write("2. The average colour values are outside the warning thresholds.")
            st.write("3. The food appears acceptable based on this basic colour analysis.")

            st.subheader("RECOMMENDATION")

            st.write("Continue with normal food inspection.")

        # Step 7: Final report

        st.divider()

        st.subheader("FRESHCHECK SUMMARY")

        st.write("Food Appearance:", result)
        st.write("Average Hue:", round(hue, 2))
        st.write("Average Saturation:", round(saturation, 2))
        st.write("Average Brightness:", round(brightness, 2))

        st.info(
            "This is an experimental image-based colour check. "
            "It cannot confirm whether food is safe to eat."
        )

else:

    st.info("Please upload an image to begin your food quality check.")
