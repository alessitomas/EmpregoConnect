import json
def extract_job_info(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        job_info = {}

        # Extract job title, company, and apply link
        job_info['Cargo'] = lines[0].strip()
        job_info['Empresa'] = lines[2].strip()
        job_info['Link para aplicar'] = lines[1].strip()

        # Extract minimum qualifications
        min_qual_index = lines.index('Minimum qualifications:\n')
        min_qual_end_index = lines.index('Preferred qualifications:\n')
        minimum_qualifications = [line.strip() for line in lines[min_qual_index+1:min_qual_end_index]]
        job_info['Minimum qualifications'] = minimum_qualifications

        
        # Extract preferred qualifications
        pref_qual_index = min_qual_end_index
        pref_qual_end_index = lines.index('About the job\n')
        preferred_qualifications = [line.strip() for line in lines[pref_qual_index+1:pref_qual_end_index]]
        job_info['Preferred qualifications'] = preferred_qualifications

        
        # Extract responsibilities
        resp_index = lines.index('Responsibilities\n')
        responsibilities = [line.strip() for line in lines[resp_index+1:]]
        job_info['Responsibilities'] = responsibilities

        

        return job_info


jobs_details = []

for i in range(1,21):
    
    job_info = extract_job_info(f"data/job{i}.txt", sum)
    jobs_details.append(job_info)


with open('data/jobs_details.json', 'w') as f:
    json.dump(jobs_details, f)
