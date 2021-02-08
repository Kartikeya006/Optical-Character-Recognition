import core
import cv2

test_image_names = core.find_path()

f = open("Output.txt", 'w')
for i in list(test_image_names):
    i = "test_images/"+i
    image = cv2.imread(i)
    extracted_text  = core.ocr_core(image)
    f.write(f"[{i}]:-\n{extracted_text}\n\n")
    core.show_box(image, i)

f.close()
