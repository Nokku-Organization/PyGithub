from github import Github
g = Github("<github-personal-token>")

#Get repositories for an organization
org = g.get_organization('Nokku-Organization')
repos = org.get_repos()
print(repos)
repos_id_list=[]

"""
for repo in repos:
	repos_id_list.append(repo.name)
        contents = repo.get_contents("README.md")
        print(contents.sha)

print(repos_id_list)
"""

repo = g.get_repo("Nokku-Organization/testing-repo-1")

source_branch = 'master'
target_branch = 'newfeature'


sb = repo.get_branch(source_branch)
#repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)  ##this line of code is for creation of new branch(target_branch) from existing source_branch


generated_vpc_cidr='"10.0.0.0/16"'
vpcModuleText='''module "vpc" { 
  source = "terraform-aws-modules/vpc/aws"
  name = "my-vpc"
  cidr = %s
  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  enable_nat_gateway = true
  enable_vpn_gateway = true
  tags = {
    Terraform = "true"
    Environment = "dev"
  }
}
'''%(generated_vpc_cidr)
#.format('vpc_cidr'="test")
#repo.create_file("region/infrastructure/vpc.tf", "commit-vpc", "contect-vpc-with-cidr", branch= target_branch)
repo.create_file("region/infrastructure/vpccidr2.tf", "commit-vpc", vpcModuleText, branch= target_branch)





