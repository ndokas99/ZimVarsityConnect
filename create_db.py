from sqlite3 import connect


def write():
    con = connect("universities.db")

    universities = [["University of Zimbabwe", "uz", "Knowledge, Diligence and Integrity", "University of Zimbabwe<br>P.O. Box MP 167<br>Mt. Pleasant<br>Harare", "tel: +263242303211", "https://www.uz.ac.zw"],
                    ["Great Zimbabwe University", "gzu", "Knowledge, Culture and Development", "Great Zimbabwe University<br>P.O Box 1235<br>Masvingo<br>Zimbabwe", "cell: +263782780662", "https://www.gzu.ac.zw/"],
                    ["Women's University in Africa", "wua", "Addressing Gender Disparity and Fostering Equality in University Education", "Women's University in Africa<br>P.O. Box GD 32 Greendale<br>549 Arcturus Road<br>Manresa<br>Harare", "tel: +263242459601", "http://www.wua.ac.zw"],
                    ["Chinhoyi University of Technology", "cut", "Technology, Innovation, Entrepreneurship and Wealth Creation", "Chinhoyi University of Technology<br>Private Bag 7724<br>Chinhoyi<br>Zimbabwe", "tel: +263 6721 22203-5", "https://www.cut.ac.zw"],
                    ["Zimbabwe Open University", "zou", "Empowerment Through Open Learning", "Zimbabwe Open University<br>Box 1810 Gweru<br>No. 16 Victory Road<br>Gweru East", "tel: +263 54 226002/3", "http://www.zou.ac.zw"],
                    ["Midlands State University", "msu", "Our Hands, Our Minds, Our Destiny", "Midlands State University<br>Private Bag 9055<br>Senga Road<br>Gweru", "tel: +263-54-2260359", "https://ww5.msu.ac.zw"]]

    for (univ, img, motto, addr, tel, email) in universities:
        con.execute("insert into university values (?, ?, ?, ?, ?, ?)", (univ, img, motto, addr, tel, email))
        con.commit()

    faculties = [["MEDICINE & HEALTH SCIENCES", "ARTS & HUMANITIES", "BUSINESS MANAGEMENT SCIENCES AND ECONOMICS"],
                 ["SCHOOL OF AGRICULTURE AND NATURAL SCIENCES", "SCHOOL OF COMMERCE", "SCHOOL OF SOCIAL SCIENCES"],
                 ["AGRICULTURAL SCIENCES", "MANAGEMENT AND ENTREPRENEURIAL SCIENCES", "SOCIAL AND GENDER TRANSFORMATIVE SCIENCES"],
                 ["NATURAL SCIENCES & MATHEMATICS", "ART & DESIGN", "ENTREPRENEURSHIP & BUSINESS SCIENCES"],
                 ["APPLIED SOCIAL SCIENCES", "COMMERCE AND LAW", "SCIENCE"],
                 ["AGRICULTURE, ENVIRONMENT AND NATURAL RESOURCES MANAGEMENT", "BUSINESS SCIENCES", "ARTS AND HUMANITIES"]]

    num = 0
    for group in faculties:
        for faculty in group:
            con.execute("insert into faculty values (?, ?)", (faculty, universities[num][0]))
            con.commit()
        num += 1

    data = [['BSc Hons in Audiology', '4yrs', 10, '3 Advanced level passes including Biology and any 2 from Maths,Physics and Chemistry'],
            ['B. Pharmacy Hons.', '4yrs', 13, "3 'A' Level passes in Chemistry (Compulsory) & any two of Biology, Physics or Maths."],
            ['Bachelor of Medicine and Bachelor of Surgery', '6yrs', 15, "3 'A' Level passes in Chemistry (Compulsory) & any 2 of Biology, Physics or Maths."],
            ['BA Honours Film Radio and Television Production', '4yrs', 6, "At least 2 'A' level in Arts subjects"],
            ['BA Honours Media and Marketing Communication', '4yrs', 6, "At least 2 ''A'' level passes in Arts subjects or Commercials"],
            ['BA Honours Philosophy Ethics and Human Development', '4yrs', 6, "'A' Level passes in Arts subjects plus 5 'O' Level Subjects including English language Or A diploma in Philosophy from a recognised institution"],
            ['BSc Honours Accounting and Finance', '4yrs', 14, 'At least 2 ''A'' Level passes plus 5 ''O Level passes including Maths and English Language or Relevant diploma or equivalent as prescribed under the National Qualifications Framework'],
            ['BSc Honours Business Management Systems Design and Applications', '4yrs', 10, 'At least 2 ''A'' Level passes plus 5 ''O Level passes including Maths and English Language or Relevant diploma or equivalent as prescribed under the National Qualifications Framework'],
            ['BSc Honours Business and Industrial Economics', '4yrs', 10, 'At least 2 ''A'' Level passes plus 5 ''O Level passes including Maths and English Language or Relevant diploma or equivalent as prescribed under the National Qualifications Framework'],

            ['Bachelor of Science Honours Degree in Geography and Environmental Science', '4 years Conventional/ 3 years Block Release','',"Normal Entry\na) At least five (5) 'O' level passes including English Language and Mathematics at Grade C or better.\nb) At least two (2) 'A' level passes in the relevant subjects or their recognised equivalents.\nSpecial Entry\nCandidates who possess a Certificate/Diploma in Education in which Geography, Mathematics, Computer Science, Physics or its recognised equivalent is one of the major subjects studied will also be considered."],
            ['Bachelor of Science Honours Degree in Agriculture (Soil and Plant science)', '4 years Conventional/ 3 years Block Release for candidates who are already working in a related area of specialization','',"Normal Entry\na) At least five (5) 'O' level passes including English Language and Mathematics at Grade C or better.\nb) At least two (2) 'A' level passes in any of the following subjects: Agriculture, Chemistry, Physics, Biology, Geography and Mathematics.\nSpecial Entry\na) At least five (5) 'O' level passes including English Language, Geography and any Science Subject at Grade C or better.\nb) Candidates should possess a Diploma in Agriculture/ Horticulture/ Forestry or any relevant Diploma from a recognised College/ University"],
            ['Bachelor of Science Honours Degree (Computer Sciences)', '1 year block release', '', "Normal Entry\na) At least five (5) 'O' level passes including English Language and Mathematics at Grade C or better.\nb) At least two (2) 'A' level passes in the relevant subjects or their recognised equivalents.\nc) At least two (2) 'A' level passes including Mathematics or its recognized equivalents.\nSpecial Entry\nCandidates who possess a Certificate/Diploma in Education in which Geography, Mathematics, Computer Science, Physics or its recognised equivalent is one of the major subjects studied will also be considered."],
            ["Bachelor of Commerce Honours in Accounting", "(4 Years Conventional/ Parallel)(3 Years Parallel/ Block Release for candidates who are already working in a related area of specialization)", "", "Normal Entry\na) Five (5) 'O' level passes or equivalent including English Language and Mathematics at grade C or better.\nb) 2 'A' level passes including at least onecommercial subject or Mathematics.\nc) In approved cases, holders of an appropriate Higher National Diploma may qualify for entry into the programmes.\nApplicants for Block Release Programmes must attach Confirmation of Employment letters that include their duties and duration of employment on current job."],
            ["Bachelor of Commerce Honours in Banking and Finance", "(4 Years Conventional/ Parallel)(3 Years Parallel/ Block Release for candidates who are already working in a related area of specialization)", "", "Normal Entry\na) Five (5) 'O' level passes or equivalent including English Language and Mathematics at grade C or better.\nb) 2 'A' level passes including at least onecommercial subject or Mathematics.\nc) In approved cases, holders of an appropriate Higher National Diploma may qualify for entry into the programmes.\nApplicants for Block Release Programmes must attach Confirmation of Employment letters that include their duties and duration of employment on current job."],
            ["Bachelor of Commerce Honours in Office Management", "(4 Years Conventional/ Parallel)(3 Years Parallel/ Block Release for candidates who are already working in a related area of specialization)", "", "Normal Entry\na) Five (5) 'O' level passes or equivalent including English Language and Mathematics at grade C or better.\nb) 2 'A' level passes including at least onecommercial subject or Mathematics.\nc) In approved cases, holders of an appropriate Higher National Diploma may qualify for entry into the programmes.\nApplicants for Block Release Programmes must attach Confirmation of Employment letters that include their duties and duration of employment on current job.\nOffice Management and Internal Auditing are offered on a block release basis only."],
            ["Bachelor of Science Honours in Psychology", "4 Years Conventional/ 3 years Parallel/ Block Release", "", "a) At least five (5) 'O' Level passes including English Language at Grade C or better.\nb) At least five (5) 'O' Level passes including English Language and Mathematics and any other science subject deemed relevant by the host department.\nc) At least two (2) 'A' Level passes.\ne) Applicants who do not meet normal entry requirements, may, subject to the approval of the Senate, be admitted through Special Entry (for block release programmes only)"],
            ["Bachelor of Science Honours in Urban Planning and Development", "4 Years Conventional/ 3 years Parallel/ Block Release", "", "a) At least five (5) 'O' Level passes including English Language at Grade C or better.\nb) At least five (5) 'O' Level passes including English Language and Mathematics.\nc) At least two (2) 'A' Level passes.\ne) Applicants who do not meet normal entry requirements, may, subject to the approval of the Senate, be admitted through Special Entry (for block release programmes only)"],
            ["Bachelor of Science Honours in Sociology", "4 Years Conventional/ 3 years Parallel/ Block Release", "", "a) At least five (5) 'O' Level passes including English Language at Grade C or better.\nb) At least two (2) 'A' Level passes.\ne) Applicants who do not meet normal entry requirements, may, subject to the approval of the Senate, be admitted through Special Entry (for block release programmes only)"],

            ["Bachelor of Science Agriculture Honours Degree in Animal Science", "4yrs", "", "At least two 'A' level passes in any Science subjects with at least five 'O' level subjects including Mathematics and English; OR\nAt least a Diploma in Agriculture from a recognised institution after attaining a minimum of five 'O' level passes including English Language and Mathematics; OR\nAt least a Diploma in Veterinary Science from a recognised institution after attaining a minimum of five 'O' level passes including English Language and Mathematics\nAny other relevant qualification from a recognised institution"],
            ["Bachelor of Science Agriculture Honours Degree in Horticulture", "4yrs", "", "At least two 'A' level passes in any Science subjects with at least five 'O' level subjects including Mathematics and English; OR\nAt least a Diploma in Agriculture from a recognised institution after attaining a minimum of five 'O' level passes including English Language and Mathematics; OR\nAt least a Diploma in Veterinary Science from a recognised institution after attaining a minimum of five 'O' level passes including English Language and Mathematics\nAny other relevant qualification from a recognised institution"],
            ["Bachelor of Science Honours Degree in Integrated Environmental Management", "4yrs", "", "At least two 'A' level passes in any Science subjects with at least five 'O' level subjects including Mathematics and English; OR\nAt least a Diploma in Environmental Management from a recognised institution after attaining a minimum of five 'O' level passes including English Language and Mathematics"],
            ["Bachelor of Accounting Science Honours Degree", "4yrs", "", "Minimum of five 'O' level passes including English Language and Mathematics, and At least two 'A' level passes in Commercial subjects; OR\nA Diploma of a finance related qualification or an accountancy diploma e.g. CIS, ACCA or HND with at least 2 years relevant work experience. "],
            ["Bachelor of Science Honours Degree in Computer Science", "4yrs", "", "Minimum of five 'O' level passes including English Language and Mathematics; and \nAt least two 'A' level passes in relevant subjects; OR\nA relevant Diploma in Computer Science/Computer Studies/ Information Technology and at least 2 years relevant work experience."],
            ["Bachelor of Science Honours Degree in Business Intelligence and Data Analytics", "4yrs", "", "Minimum of five 'O' level passes including English Language and Mathematics; and\nAt least two 'A' level passes in Science and/or Commercial subjects"],
            ["Bachelor of Science Honours Degree in Social Work", "4yrs", "", "Minimum of five 'O' Level passes including English Language and at least relevant 'A' levels passes; OR\nA minimum of five 'O' Level passes including English Language and a Diploma in Social Work."],
            ["Bachelor of Science Honours Degree in Psychology", "4yrs", "", "Minimum of five 'O' Level passes including English Language and at least relevant 'A' levels passes; OR\nA minimum of five 'O' Level passes including English Language and any relevant diploma."],
            ["Bachelor of Education Degree (Primary) In Service", "3yrs", "", "A minimum of five 'O' Level passes including English Language and a Diploma in Education."],

            ["Bachelor of Science (Hons) degree in Physics with majors in Computational Physics", "4yrs", "", "'A' level pass in Physics and Mathematics"],
            ["Bachelor of Science (Hons)  degree in Mathematics  or Statistics with Majors in Scientific Computing", "4yrs", "", "'A' level pass in Mathematics and at least one of the following  'A' level subjects; Biology, Chemistry, Computer Science and Physics"],
            ["Bachelor of Science (Hons) degree in Chemistry with Majors in Medicinal Chemistry", "4yrs", "", "'A' level pass in Chemistry and at least one of the following subjects: Mathematics, Physics or Biology"],
            ["Bachelor of Science (Hons) degree in Creative Art and Design", "4yrs", "", "2 'A' Level passes one of which should be Art and Design. A National Diploma in Art and Design or a recognized teaching qualification with specialization in Art and Design."],
            ["Bachelor of Science (Hons) degree in Clothing Fashion Design", "4yrs", "", "2 'A' level passes. A pass in Textiles & Clothing Design is an added advantage or an Advanced or National Diploma in a relevant field."],
            ["Bachelor of Science (Hons) degree in Fine Art", "4yrs", "", "2 'A' level passes. A pass in Art & Design at 'A' level is an added advantage.  A National Diploma in Art and Design or a recognized teaching qualification with specialization in Art and Design."],
            ["Bachelor of Science (Hons) degree in Accountancy", "4yrs", "", "2 'A' Level passes which must include Accounting and commercial related subjects from the following: Economics, Accounting, Mathematics, Geography, Statistics, and Computers."],
            ["Bachelor of Science (Hons) degree in Entrepreneurship and Business Management", "4yrs", "", "2 'A' Level passes. Preference will be given to passes in commercially related subjects like Management Of Business, Economics, Accounting, Mathematics, Sociology and Geography"],
            ["Bachelor of Science (Hons) degree in Marketing", "4yrs", "", "2 'A' Level passes. Preference will be given to passes in commercially related subjects like Management Of Business, Economics, Accounting, Mathematics, Geography, Statistics, and Computers"],

            ["Bachelor of Science Honours in Psychology", "4yrs", "", "A minimum of 5 'O' Level passes or equivalent including English Language and Mathematics at Grade C or better"],
            ["Bachelor of Science Honours in Records And Archives Management", "4yrs", "", "Applicants must have 5 'O' level passes, including English Language at Grade C or better OR Gained advanced standing through the Accreditation of Prior Learning route."],
            ["Bachelor of Science Honours in Library And information Technology", "2yrs", "", "A minimum of 5 'O' Level passes including English Language at Grade C or better; AND a Higher National Diploma in Library and Information Science"],
            ["Bachelor of Commerce in Accounting (Honours)", "4yrs", "", "A minimum of 5 'O' Level passes including English Language and Mathematics at Grade C or better at Grade C or better"],
            ["Bachelor of Commerce in Banking And Finance (Honours)", "4yrs", "", "A minimum of 5 'O' Level passes including English Language and Mathematics at Grade C or better at Grade C or better"],
            ["Bachelor of Commerce in Marketing Management", "4yrs", "", "A minimum of 5 'O' Level passes including English Language and Mathematics at Grade C or better at Grade C or better"],
            ["Bachelor of Science Honours in Nursing Science", "4yrs", "", "A minimum of 5 'O' Level passes including English language and a 1.5 BACHELOR OF COMMERCE IN MARKETING prior learning (APL) route Science subject at Grade C or better or their equivalent. Applicants must MANAGEMENT (HONOURS) (4 YEARS) have a Diploma in Nursing and be registered with the Nurses Council of Zimbabwe. Please note that two years post qualification experience is a requirement."],
            ["Bachelor of Science Honours in Physical Education And Sport", "4yrs", "", "A minimum of 5 'O' level passes, including English Language and a 1.7 BACHELOR OF COMMERCE IN HUMAN RESOURCE, Science subject with a grade “C” or better. Or A relevant INDUSTRIAL & LABOUR RELATIONS MANAGEMENT Entry requirements: diploma/certificate or 'A' Level science passes will be an added advantage"],
            ["Bachelor of Science Honours in Mathematics And Statistics", "4yrs", "", "A minimum of 5 'O' Level passes including English Language, Mathematics and Science at Grade C or better. A pass at 'A' level Mathematics or a teachers' certificate or Diploma in Education with Mathematics as a major subject will be an added advantage"],

            ["Bachelor of Science Honours in Agricultural Economics and Development", "4yrs", "", "'O' Level Mathematics and any Two 'A' Level Science subjects in Agriculture, Mathematics, Economics, Management of Business, Sociology, Accounts, Geography and Biology"],
            ["Bachelor of Science Honours in Agricultural Water Management and Technology", "5yrs", "", "'O' Level Mathematics and any Two 'A' Level Science subjects in Biology/ Agriculture and any Sciences"],
            ["Bachelor of Science Honours in Animal Product Processing Technology", "4yrs", "", "'O' Level Mathematics and any Two 'A' Level Science subjects in Business, Sociology, Accounts, Geography and Biology"],
            ["Bachelor of Commerce in Agritourism Management", "4yrs", "", "'O' Level Mathematics is a requirement and Two 'A' Level passes in any subject"],
            ["Bachelor of Commerce in Applied Accounting", "4yrs", "", "'O' Level Mathematics is a requirement and A' Level Accounting plus any two Commercial subjects"],
            ["Bachelor of Commerce in Cloud Computing and Internet of Things", "4yrs", "", "'O' Level Mathematics is a requirement and A' level Mathematics and a pass in any of the following subjects or their equivalents: Accounting, Economics, Management of Business and Computer Studies"],
            ["Bachelor of Arts Honours in Development Planning and Management", "4yrs", "", "Any two 'A' Level passes in Arts, Humanities and Social Sciences subjects"],
            ["Bachelor of Arts Honours in Development Practice", "4yrs", "", "Any two 'A' Level passes in Arts, Humanities and Social Sciences subjects"],
            ["Bachelor of Arts Honours in Digital Archival and Historical Information Management", "4yrs", "", "History and any Arts/Humanities subjects"]]

    x = 0
    num = 0
    for group in faculties:
        for faculty in group:
            for _ in range(3):
                con.execute("insert into degrees values (?,?,?,?,?,?)",
                            (data[x][0], data[x][1], data[x][2], data[x][3], faculty, universities[num][0]))
                con.commit()
                x += 1
        num += 1
