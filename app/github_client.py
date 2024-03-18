from github import Github

class GitHubClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.client = Github(access_token)

    def authenticate(self):
        try:
            user = self.client.get_user()
            print(f"Authenticated as: {user.login}")
        except Exception as e:
            print(f"Authentication failed: {str(e)}")

    def create_repo(self, name, description=None, private=False):
        try:
            repo = self.client.get_user().create_repo(
                name=name,
                description=description,
                private=private
            )
            print(f"Repository '{name}' created successfully!")
            return repo
        except Exception as e:
            print(f"Failed to create repository: {str(e)}")
            return None

    def create_pull_request(self, repo, title, head_branch, base_branch, body=None):
        try:
            pr = repo.create_pull(
                title=title,
                body=body,
                head=head_branch,
                base=base_branch
            )
            print(f"Pull request '{title}' created successfully!")
            return pr
        except Exception as e:
            print(f"Failed to create pull request: {str(e)}")
            return None