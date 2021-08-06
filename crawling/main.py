from indeed import extrat_indeed_pages, extract_indeed_jobs

last_page = extrat_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_page)
print(indeed_jobs)



