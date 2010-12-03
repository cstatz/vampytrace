 %module VT_User
 %{
 /* Includes the header in the wrapper code */
 #include "vt_user.h"
 %}
 
 /* Parse the header file to generate wrappers */
 %include "vt_user.h"
 %include "vt_user_control.h"
 %include "vt_user_comment.h"
 %include "vt_user_count.h"
 %include "vt_user_marker.h"
 %include "vt_user_region.h"
