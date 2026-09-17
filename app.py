import sys
from analytics_engine import AcademicAnalyticsSystem

def main():
    print("====================================================")
    print("      STUDENT PERFORMANCE PIPELINE MANAGEMENT       ")
    print("====================================================")
    
    input_db = "students.csv"
    output_report = "student_report.txt"
    
    try:
        # Instantiate and run the analytic engine system pipeline
        system = AcademicAnalyticsSystem(input_db)
        system.load_and_parse_records()
        system.generate_aggregated_report(output_report)
        
        print("[SUCCESS] Analytical metrics successfully compiled and processed.")
        print("====================================================")
        
    except Exception as e:
        print(f"[FATAL FAILURE] Operational failure interrupted workflow execution: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
