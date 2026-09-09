from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="CloudXeus Portal")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CloudXeus Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>body { font-family: 'Inter', sans-serif; }</style>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen flex items-center justify-center p-4">
        <div class="max-w-md w-full bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl relative overflow-hidden">
            <!-- Glow background effect -->
            <div class="absolute -top-10 -right-10 w-32 h-32 bg-indigo-500/10 rounded-full blur-2xl"></div>
            
            <div class="flex items-center justify-between mb-6">
                <div class="flex items-center space-x-3">
                    <div class="h-10 w-10 rounded-xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400 font-bold text-xl">
                        ☁️
                    </div>
                    <div>
                        <h1 class="text-lg font-bold text-white tracking-wide">CloudXeus</h1>
                        <p class="text-xs text-slate-400">System Overview</p>
                    </div>
                </div>
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"></span>
                    Running
                </span>
            </div>

            <div class="space-y-4">
                <div class="bg-slate-950/60 border border-slate-800/80 rounded-xl p-4">
                    <p class="text-xs uppercase tracking-wider text-slate-500 font-semibold mb-1">Message</p>
                    <p class="text-slate-200 font-medium">Hello from CloudXeus!</p>
                </div>
                
                <div class="grid grid-cols-2 gap-3 text-xs">
                    <div class="bg-slate-950/40 border border-slate-800/50 p-3 rounded-lg">
                        <span class="text-slate-500 block">Framework</span>
                        <span class="text-slate-300 font-medium">FastAPI</span>
                    </div>
                    <div class="bg-slate-950/40 border border-slate-800/50 p-3 rounded-lg">
                        <span class="text-slate-500 block">Response Time</span>
                        <span class="text-slate-300 font-medium">&lt; 1ms</span>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """