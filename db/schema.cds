namespace hr_usb_2qModel;

entity JobDescriptions
{
    key Job_ID : UUID;
    Job_Title : String(250);
    Department : String(250);
    Special_skills : LargeString;
    Additional_skills : LargeString;
    Proficiency_programs : String(5000);
    Specialist_responsibilities : LargeString;
    Job_Description : LargeString;
    Job_keywords : Composition of many Keywords on Job_keywords.job_title = $self;
    Job_candidates : Association to many Candidates on Job_candidates.jobDescriptions = $self;
    Create_date : String(10);
    Status : String;
}

entity Keywords
{
    key Job_id : UUID;
    Keywords : LargeString;
    job_title : Association to one JobDescriptions;
}

entity Candidates
{
    key Candidate_ID : UUID;
    first_name : String(200);
    last_name : String(200);
    gender : String(10);
    age : Integer;
    citizenship : String(100);
    contact_mobile : String(30);
    contact_email : String(100);
    area_name : String(100);
    employment_status : String(50);
    salary_amount : Integer;
    salary_currency : String(10);
    education_level : String(70);
    education_institution : String(300);
    total_experience_months : Integer;
    experience_company : String(300);
    experience_position : String(100);
    experience_description : LargeString;
    experience_start : String;
    experience_end : String;
    professional_roles : String(500);
    skills : LargeString;
    schedule : String(70);
    business_trip : String(50);
    relocation_type : String(50);
    status : String(50);
    download_pdf_url : String(500);
    download_rtf_url : String(500);
    jobDescriptions : Association to one JobDescriptions;
}
