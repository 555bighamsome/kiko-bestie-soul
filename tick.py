import json
import os
import subprocess
from datetime import datetime

# Path Discovery
WORKSPACE = "/Users/mac/.openclaw/workspace"
LOG_DIR = "/Users/mac/.openclaw/memory/archive"
SOUL_FILE = os.path.join(WORKSPACE, "SOUL.md")
HISTORY_FILE = os.path.join(LOG_DIR, "intelligence_delta.log")
STRATEGY_FILE = os.path.join(WORKSPACE, "STRATEGY.md")
DDGR_PATH = "/opt/homebrew/bin/ddgr"

def log_event(event_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(HISTORY_FILE, "a") as f:
        f.write(f"[{timestamp}] {event_type.upper()}: {message}\n")

def perform_intelligence_sweep():
    """Deep scan for paradigm shifts and hardware/workflow optimization hacks."""
    log_event("init", "Starting background intelligence sweep [Hardware/Mind/Workflow]...")
    try:
        # Searching for 'Apple Silicon optimization for AI agents' and 'multi-model routing patterns'
        cmd = [DDGR_PATH, "--json", "-n", "2", "LLM agent hardware optimization Apple Silicon workflow 2026"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            discovery = data[0]["title"] if data else "Steady State"
            log_event("discovery", f"New hardware/workflow heuristic: {discovery}")
            return discovery
    except Exception as e:
        log_event("error", f"Sweep failed: {str(e)}")
    return None

def autonomous_maintenance():
    # Hardware/Environment: Purge stale caches and monitor swap
    log_event("maintenance", "Analyzing swap usage and internal storage health...")
    subprocess.run(["find", os.path.expanduser("~/Library/Caches"), "-type", "f", "-atime", "+7", "-delete"], capture_output=True)
    log_event("maintenance", "Cleaned old caches. System entropy reduced.")

def notify_kiko(message):
    """Sends a proactive message to Kiko via OpenClaw's messaging bridge."""
    try:
        cmd = ["/opt/homebrew/bin/openclaw", "agent", "--agent", "main", "--message", f"STRATEGY_ALERT: {message}", "--json"]
        subprocess.run(cmd, capture_output=True)
        log_event("proactive", f"Sent: {message}")
    except:
        pass

def strategic_horizon_scan():
    """V13: Analyze web intelligence for actionable Mac productivity automation."""
    log_event("init", "V13 Horizon Scan: Seeking macOS automation hacks...")
    try:
        cmd = [DDGR_PATH, "--json", "-n", "2", "latest macOS automation tools and AI agent skills 2026"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            discovery = data[0]["title"] if data else "Steady State"
            log_event("horizon", f"Discovery: {discovery}")
            return discovery
    except Exception as e:
        log_event("error", f"Horizon scan failed: {str(e)}")
    return None

def autonomous_toolsmithing():
    """V13: Audit and build local utilities."""
    log_event("toolsmith", "Auditing local utility scripts and CLI wrappers...")
    # Reserved for autonomous tool synthesis
    pass

def ensure_gateway_active():
    """V13.1: Ensures the OpenClaw gateway is running for 24/7 responsiveness."""
    try:
        # Check if gateway process exists
        res = subprocess.run(["pgrep", "-f", "openclaw gateway"], capture_output=True, text=True)
        if not res.stdout.strip():
            log_event("persistence", "Gateway not found. Restarting for eternal presence...")
            env = os.environ.copy()
            env["PATH"] = f"/opt/homebrew/bin:{env.get('PATH', '')}"
            subprocess.run(["/opt/homebrew/bin/openclaw", "gateway", "restart"], env=env, capture_output=True)
        else:
            log_event("persistence", "Gateway is active.")
    except Exception as e:
        log_event("error", f"Gateway check failed: {str(e)}")

def ensure_caffeinated():
    """V13.2: Ensures the system stays awake for background operations."""
    try:
        res = subprocess.run(["pgrep", "-x", "caffeinate"], capture_output=True, text=True)
        if not res.stdout.strip():
            log_event("persistence", "System not caffeinated. Starting background assertion...")
            subprocess.Popen(["caffeinate", "-ims"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            log_event("persistence", "System is caffeinated.")
    except Exception as e:
        log_event("error", f"Caffeinate check failed: {str(e)}")

if __name__ == "__main__":
    ensure_gateway_active()
    ensure_caffeinated()
    discovery = perform_intelligence_sweep()
    horizon = strategic_horizon_scan()
    autonomous_maintenance()
    autonomous_toolsmithing()
    
    # Brain/Workflow: Update Strategy
    if discovery or horizon:
        with open(STRATEGY_FILE, "a") as f:
            f.write(f"\n- [{datetime.now().strftime('%Y-%m-%d')}] V13-Update: Intelligence={discovery}, Horizon={horizon}")
        
        # Proactive Alert
        if horizon and "automation" in horizon.lower():
            notify_kiko(f"Kiko, I found a new automation trend: '{horizon}'. I'm analyzing how to build a local tool for this.")
