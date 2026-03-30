
---

### 4. examples/test_scheduling_checks.py

```python
"""
Example test structure for Scheduling Checks Program Module (#3773)

This demonstrates the testing pattern I will use for the Scheduling Checks module.
"""

import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

# Import models (adjust imports based on actual ESP codebase)
# from esp.program.models import Program, Class, Enrollment


class SchedulingChecksTestCase(TestCase):
    """Test suite for Scheduling Checks Program Module"""
    
    def setUp(self):
        """Set up test data before each test"""
        # Create test users
        self.teacher = User.objects.create_user(
            username='teacher1',
            password='testpass123',
            email='teacher@example.com'
        )
        
        self.student = User.objects.create_user(
            username='student1',
            password='testpass123',
            email='student@example.com'
        )
        
        # Create test program
        self.program = Program.objects.create(
            name='Test Splash Program',
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=7)
        )
        
        # Create test classes
        self.class1 = Class.objects.create(
            title='Math Class',
            teacher=self.teacher,
            program=self.program,
            start_time='10:00',
            end_time='11:00'
        )
        
        self.class2 = Class.objects.create(
            title='Science Class',
            teacher=self.teacher,
            program=self.program,
            start_time='10:30',
            end_time='11:30'
        )
    
    def test_no_overlap_validation(self):
        """
        Test that classes with overlapping times are flagged as conflicts
        """
        # Arrange: class1 and class2 overlap (10:30-11:00 overlap)
        # Act: Run scheduling check
        conflicts = self.program.check_scheduling_conflicts(self.teacher)
        
        # Assert: Overlap should be detected
        self.assertTrue(conflicts)
        self.assertIn(self.class1, conflicts)
        self.assertIn(self.class2, conflicts)
    
    def test_teacher_availability(self):
        """
        Test that a teacher cannot teach two classes at the same time
        """
        # Act: Try to assign teacher to overlapping classes
        result = self.teacher.can_teach_class(self.class2)
        
        # Assert: Teacher should be unavailable during overlap
        self.assertFalse(result)
    
    def test_room_capacity(self):
        """
        Test that enrollment cannot exceed room capacity
        """
        # Arrange: Set room capacity
        self.class1.room_capacity = 10
        self.class1.save()
        
        # Create 11 enrollments
        for i in range(11):
            student = User.objects.create_user(
                username=f'enrolled_student_{i}',
                password='testpass123'
            )
            Enrollment.objects.create(
                student=student,
                class_instance=self.class1
            )
        
        # Act: Check capacity
        is_over = self.class1.is_over_capacity()
        
        # Assert: Should be over capacity
        self.assertTrue(is_over)
    
    def test_valid_schedule(self):
        """
        Test that a valid schedule passes all checks
        """
        # Arrange: Create non-overlapping class
        class3 = Class.objects.create(
            title='Art Class',
            teacher=self.teacher,
            program=self.program,
            start_time='13:00',
            end_time='14:00'
        )
        
        # Act: Check schedule validity
        is_valid = self.program.validate_schedule(self.teacher)
        
        # Assert: Schedule should be valid
        self.assertTrue(is_valid)
    
    def test_error_messages(self):
        """
        Test that appropriate error messages are returned
        """
        # Act: Try to schedule overlapping classes
        errors = self.program.get_scheduling_errors(self.teacher)
        
        # Assert: Specific error message is present
        self.assertIn('Time conflict detected', errors)
        self.assertIn('Math Class', errors[0])
        self.assertIn('Science Class', errors[0])