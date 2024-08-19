import cv2
import os
import random
def generate_video_from_images(image_folder, output_video, frame_rate, display_time, captions=None):
    # Get list of images in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()  # Sort images by name

    # Check if there are any images
    if not images:
        print("No images found in the directory.")
        return

    # Get the size of the first image
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For mp4 file
    video = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    for idx, image in enumerate(images):
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        frames_per_image = frame_rate * display_time
        
         # Add caption if provided
        if captions and idx < len(captions):
            caption = captions[idx]
            # Position for the text (bottom center)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_thickness = 2
            text_size = cv2.getTextSize(caption, font, font_scale, font_thickness)[0]
            text_x = (width - text_size[0]) // 2
            text_y = height - 30  # 30 pixels from the bottom
            cv2.putText(frame, caption, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
            
        for _ in range(frames_per_image):
            video.write(frame)
    

    # Release the video writer object
    video.release()
    print(f"Video saved as {output_video}")

# Parameters
image_folder = '../uploads'
output_video = 'output_video.mp4'
frame_rate = 30  # Frames per second (1 frame per second)
display_time=5
captions = [
    "This is Bird 1",
    "This is Bird 2"
]

# Generate video
generate_video_from_images(image_folder, output_video, frame_rate, display_time, captions)

