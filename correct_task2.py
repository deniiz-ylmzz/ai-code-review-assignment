import re

def count_valid_emails(emails):
    count = 0
    
    valid_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    for email in emails:
        if email.count('@') == 1:
            local, domain = email.split('@')
            
            if len(local) == 0 or len(domain) == 0:
                continue
            
            local_pattern_unquoted = r'^[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]+(\.[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]+)*$'
            
            local_pattern_quoted = r'^"((?:[^"\\]|\\[\x20-\x7E])+)"$'
            
            domain_pattern = r'^[A-Za-z0-9]([A-Za-z0-9\-]{0,61}[A-Za-z0-9])?$'
            
            if (not re.fullmatch(local_pattern_unquoted, local)) and (not re.fullmatch(local_pattern_quoted, local)):
                continue
            
            domain_labels = domain.split('.')
            
            if len(domain_labels) < 2:
                continue
            
            error = False
            for label in domain_labels:
                if not re.fullmatch(domain_pattern, label):
                    error = True
                    break
            if error:
                continue
            
            count += 1
    return count
