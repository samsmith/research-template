from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA

project = ProjectDefinition(
    "I will follow all the rules": "[yes / no]",
    Project={
        "Project Title": “Differences in Vaccine Hesitancy Across Different Ethnic Groups”,
        "Project Abstract": ”Comparing childhood vaccination rates pre and post COVID19…”,
        "Project Url": “https://my.ac.uk/blah”,
        "Funding Description": “UKRI”,
        "Any Highly Sensitive Items and Why": “none”,
    }
    
    Person={
        "Email Address": "$environment_variable_so_not_in_a_file",
        "Hi to the output checkers": “will send chocolate”,
        "I have done the NHS Approved Researcher training": "[yes / no]",
        "I have done all NHS AR additional modules for this data":  "[yes / no]",
        "Ethical research, so must respect dissents" : "[yes / no]",
        "<<organisational assurances>>": "[yes / no]",

        "I have had my access to a different ONS/NHS/etc safe setting revoked": "[yes / no]"
        "I am a terrorist (for the same reason as on immigration forms)": "[yes / no]"
        "I am a criminal (whatever DARS currently asks)": "[yes / no]"
    }
)

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),
)
