from playwright.sync_api import Page, expect

from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CourseExerciseFormComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
  def __init__(self, page: Page):
    super().__init__(page)

    self.create_course_form = CreateCourseFormComponent(page)

    from components.courses.create_course_exercises_toolbar_view_component import \
      CreateCourseExercisesToolbarViewComponent
    self.create_course_exercise_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)

    self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)

    self.course_exercise_form = CourseExerciseFormComponent(page)

    self.exercises_empty_view = EmptyViewComponent(page,
                                                   'create-course-exercises')
    self.image_upload_empty_view = ImageUploadWidgetComponent(page,'create-course-preview')

    self.preview_image = page.get_by_test_id(
        'create-course-preview-image-upload-widget-preview-image')

  def check_visible_exercises_empty_view(self):
    self.exercises_empty_view.check_visible(
        title='There is no exercises',
        description='Click on "Create exercise" button to create new exercise'
    )
