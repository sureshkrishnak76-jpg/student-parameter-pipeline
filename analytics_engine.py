import csv

class StudentRecord:
    """Represents a structural record for an individual student entity."""
    def __init__(self, id, name, dept, math, sci, eng, attendance):
        self.id = id
        self.name = name
        self.dept = dept
        self.math = int(math)
        self.science = int(sci)
        self.english = int(eng)
        self.attendance = int(attendance)
        self.gpa = self._calculate_gpa()
        self.status = "PASS" if self._is_passing() else "FAIL"

    def _calculate_gpa(self):
        """Computes student absolute percentage score average."""
        return round((self.math + self.science + self.english) / 3, 2)

    def _is_passing(self):
        """Evaluates academic clearance rules against individual marks."""
        return self.math >= 50 and self.science >= 50 and self.english >= 50


class AcademicAnalyticsSystem:
    """Core pipeline processing engine to extract academic metrics."""
    def __init__(self, database_path):
        self.database_path = database_path
        self.students = []
        self.department_scores = {}
        self.probation_list = []
        self.attendance_warnings = []

    def load_and_parse_records(self):
        """Loads and converts row data into manageable record objects."""
        print(f"[INFO] Initializing secure channel to database: {self.database_path}")
        with open(self.database_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = StudentRecord(
                    row['StudentID'], row['Name'], row['Department'],
                    row['Math'], row['Science'], row['English'], row['Attendance']
                )
                self.students.append(student)
                self._update_department_metrics(student)
                self._verify_risk_status(student)

    def _update_department_metrics(self, student):
        """Aggregates continuous scores down sorted branch lines."""
        if student.dept not in self.department_scores:
            self.department_scores[student.dept] = []
        self.department_scores[student.dept].append(student.gpa)

    def _verify_risk_status(self, student):
        """Runs validation checks for performance or attendance risk thresholds."""
        if student.status == "FAIL":
            self.probation_list.append(student)
        if student.attendance < 75:
            self.attendance_warnings.append(student)

    def generate_aggregated_report(self, output_path):
        """Compiles calculated business intelligence findings into structural text formats."""
        if not self.students:
            raise ValueError("[ERROR] Execution interrupted: No student database entries initialized.")

        total_enrolled = len(self.students)
        overall_gpa_avg = round(sum(s.gpa for s in self.students) / total_enrolled, 2)
        top_student = max(self.students, key=lambda s: s.gpa)

        print(f"[INFO] Compilation matching analytical models. Writing to destination: {output_path}")
        with open(output_path, "w") as f:
            f.write("====================================================================\n")
            f.write("      UNIVERSITY ACADEMIC AUDIT & PERFORMANCE ANALYTICS REPORT      \n")
            f.write("====================================================================\n")
            f.write(f" Total Active Registrations Processed : {total_enrolled}\n")
            f.write(f" Batch Grand Cumulative GPA Average   : {overall_gpa_avg}%\n")
            f.write(f" Highest Performing Student Award     : {top_student.name} ({top_student.gpa}% - {top_student.dept})\n")
            f.write("====================================================================\n\n")

            f.write("1. DEPARTMENTAL PERFORMANCE MATRIX\n")
            f.write("--------------------------------------------------------------------\n")
            for dept, scores in self.department_scores.items():
                dept_avg = round(sum(scores) / len(scores), 2)
                f.write(f" -> Department: {dept:<25} | Class Count: {len(scores):<2} | Running Average: {dept_avg}%\n")
            f.write("\n")

            f.write("2. ACADEMIC MANDATORY PROBATION REGISTRY (MARKS < 50%)\n")
            f.write("--------------------------------------------------------------------\n")
            if self.probation_list:
                for s in self.probation_list:
                    f.write(f" [CRITICAL WARNING] ID: {s.id} | Name: {s.name:<15} | GPA: {s.gpa}% | Dept: {s.dept}\n")
            else:
                f.write(" -> No current student profiles triggered academic performance thresholds.\n")
            f.write("\n")

            f.write("3. ATTENDANCE SECURITY RISK ALERTS (ATTENDANCE < 75%)\n")
            f.write("--------------------------------------------------------------------\n")
            if self.attendance_warnings:
                for s in self.attendance_warnings:
                    f.write(f" [ATTENDANCE ALERT] ID: {s.id} | Name: {s.name:<15} | Present: {s.attendance}% (Minimum 75% Required)\n")
            else:
                f.write(" -> All profiles meet minimal criteria for lecture participation standards.\n")
            f.write("====================================================================\n")
