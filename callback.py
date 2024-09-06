def callback(commit):
    if commit.author_name == "Mahmoud":
        commit.author_name = "mahmoud-alhol"
    if commit.author_email == "mahmoud.asem.w.com":
        commit.author_email = "mahmoud.asem.w@gmail.com"
