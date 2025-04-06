from rich.console import Console
from rich.progress import track
import time
import random

console = Console()

def simulate_stage(stage, steps, issues_possible=False):
    console.rule(f"[bold green]{stage}")
    for _ in track(range(steps), description=f"[cyan]{stage} in progress..."):
        time.sleep(0.5)
    if issues_possible:
        # Randomly simulate an issue
        if random.choice([True, False]):
            console.print(f"[red]Issue detected during {stage}! Flagging for remediation.[/red]")
        else:
            console.print(f"[green]{stage} completed successfully with no issues.[/green]")
    else:
        console.print(f"[green]{stage} completed successfully.[/green]")
    console.print()

def main():
    console.print("[bold magenta]Starting DevSecOps Pipeline Simulation[/bold magenta]\n")
    
    # 1. Code Commit Trigger
    simulate_stage("Code Commit Trigger", steps=5)
    
    # 2. Static Application Security Testing (SAST)
    simulate_stage("Static Application Security Testing (SAST)", steps=7, issues_possible=True)
    
    # 3. Build & Containerization
    simulate_stage("Build & Containerization", steps=5)
    
    # 4. Container Security Scan (Anchore/Clair)
    simulate_stage("Container Security Scan (Anchore/Clair)", steps=5, issues_possible=True)
    
    # 5. Dynamic Application Security Testing (DAST)
    simulate_stage("Dynamic Application Security Testing (DAST)", steps=7, issues_possible=True)
    
    # 6. Compliance & IaC Check
    simulate_stage("Compliance & IaC Check", steps=5, issues_possible=True)
    
    # 7. Deployment to Production
    simulate_stage("Deployment to Production", steps=4)
    
    # 8. Continuous Monitoring
    simulate_stage("Continuous Monitoring", steps=3)
    
    console.print("[bold magenta]DevSecOps Pipeline Simulation Completed Successfully![/bold magenta]")

if __name__ == "__main__":
    main()
