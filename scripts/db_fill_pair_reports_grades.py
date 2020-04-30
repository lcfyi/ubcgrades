"""
Imports data from Pair Reports into the database. This assumes the database has been created with the proper
models and the data exist in the project directory in /ubc-pair-grade-data.
"""

from app import create_app
from config import Config
from app.models import PAIRReportsGrade
import os
import re
import csv


def main():
    app, db = create_app(Config)

    with app.app_context():
        db.create_all()

        path_to_csv_files = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'ubc-pair-grade-data', 'pair-reports')
        # csv_files = [f for f in os.listdir(path_to_csv_files) if re.match(r'.+.csv', f)]
        for dirpath, subdirs, csv_files in os.walk(path_to_csv_files):
            for csv_file in csv_files:
                csv_reader = csv.DictReader(open(os.path.join(dirpath, csv_file)))
                # Convert to normal dictionaries
                grades_dict = [dict(ele) for ele in csv_reader]
                for row in grades_dict:
                    entry = PAIRReportsGrade(campus=row['Campus'], year=row['Year'], session=row['Session'],
                            subject=row['Subject'], course=row['Course'], detail=row['Detail'], section=row['Section'],
                            title=row['Title'], professor=row['Professor'], enrolled=row['Enrolled'], average=row['Avg'],
                            stdev=row['Std dev'], high=row['High'], low=row['Low'], num_pass=row['Pass'], num_fail=['Fail'],
                            withdrew=['Withdrew'], audit=row['Audit'], other=row['Other'], grade_0_9=row['0-9'],
                            grade_10_19=row['10-19'], grade_20_29=row['20-29'], grade_30_39=row['30-39'],
                            grade_40_49=row['40-49'], grade_lt50=row['<50'], grade_50_54=row['50-54'], grade_55_59=row['55-59'],
                            grade_60_63=row['60-63'], grade_64_67=row['64-67'], grade_68_71=row['68-71'], grade_72_75=row['72-75'],
                            grade_76_79=row['76-79'], grade_80_84=row['80-84'], grade_85_89=row['85-89'], grade_90_100=row['90-100'])
                    db.session.add(entry)
        db.session.commit()


if __name__ == "__main__":
    main()
