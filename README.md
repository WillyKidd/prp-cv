# prp-cv
## Project Description
This is a sjtu prp project for reconstructing the 3d structure of grid-like objects (eg. scaffolds) from stereo images. In our initial stage of the project, we have decided to use a NaCl (sodium chloride) crystal model as the target object, since the "nodes" (i.e. the atoms) are circular and can be relatively easily identified using hough transform. Using the following steps, we should be able to reconstruct the structure:
1. Take a stereo image pair of the target object.
2. Take some stereo images of a checkerboard pattern used for calibration.
3. Calibrate the camera. Rectify the image pair of the target object.
4. Identify the nodes in the stero image pair using hough transform. 
5. Match the same nodes in the left and right images using SURF.
6. Calculate the 3d coordinates of the nodes, using the pixel coordinates and the calibration parameters.
7. Using information of the original picture, identify whether there are "rods" connecting the nodes.
8. Plot the structure.

Our next steps include:
1. Try to replace the circular nodes (since scaffolds do not have such nodes)
2. Improve identification accuracy (not all nodes may be identified, and the identification may be wrong)
3. Improve runtime (CUDA?)

## Notes:
- Images used for calibration should be placed in the `img_original` folder.
- Calibration results are stored in `calib_results` folder. If the focus of the camera has not changed, `stereo_calibrate` does not have to be run again.

## Acknowledgements:
Part of the code for camera calibration is contributed by ve450 group 2, summer 2021.

## Tools & references:
- [Obtain pixel coordinates of a particular point](https://yangcha.github.io/iview/iview.html)
- [Stereovision package documentation](https://erget.wordpress.com/2014/02/28/calibrating-a-stereo-pair-with-python/)
- [Camera matrix](http://www.cs.cmu.edu/~16385/s17/Slides/11.1_Camera_matrix.pdf)