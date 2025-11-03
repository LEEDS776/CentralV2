#!/usr/bin/env python3
"""
Central AI V2 - Advanced AI Assistant
Main Entry Point
"""

import os
import sys
from colorama import init, Fore, Style
from core.brain import Brain
from config import config

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.RED}╔═══════════════════════════════════════════════════════╗
║                                                       ║
║              {Fore.WHITE}CENTRAL AI V2{Fore.RED}                          ║
║         {Fore.LIGHTRED_EX}Advanced AI Assistant System{Fore.RED}              ║
║                                                       ║
║  {Fore.WHITE}Version: {config.VERSION}                               {Fore.RED}║
║  {Fore.WHITE}Status: {Fore.GREEN}ONLINE{Fore.RED}                                    ║
║  {Fore.WHITE}Model: Gemini 2.0 Flash{Fore.RED}                        ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def main():
    clear_screen()
    print_banner()
    
    # Initialize AI Brain
    brain = Brain()
    
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Initializing {config.AI_NAME}...")
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} AI System Ready!\n")
    print(f"{Fore.YELLOW}[TIP]{Style.RESET_ALL} Ketik 'exit', 'quit', atau 'bye' untuk keluar")
    print(f"{Fore.YELLOW}[TIP]{Style.RESET_ALL} Ketik 'clear' untuk membersihkan layar")
    print(f"{Fore.YELLOW}[TIP]{Style.RESET_ALL} Ketik 'help' untuk bantuan\n")
    print("="*60 + "\n")
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input(f"{Fore.LIGHTBLUE_EX}You >{Style.RESET_ALL} ").strip()
            
            if not user_input:
                continue
            
            # Check for special commands
            if user_input.lower() in ['exit', 'quit', 'bye', 'keluar']:
                print(f"\n{Fore.RED}[SYSTEM]{Style.RESET_ALL} Shutting down Central AI V2...")
                print(f"{Fore.GREEN}Terima kasih sudah menggunakan Central AI! Sampai jumpa!{Style.RESET_ALL}\n")
                break
            
            if user_input.lower() == 'clear':
                clear_screen()
                print_banner()
                continue
            
            if user_input.lower() == 'help':
                print(f"\n{Fore.CYAN}[HELP] Central AI V2 Commands:{Style.RESET_ALL}")
                print("  - Tanya apapun untuk mendapat jawaban AI")
                print("  - 'clear' - Bersihkan layar")
                print("  - 'exit/quit/bye' - Keluar dari program")
                print("  - 'help' - Tampilkan pesan ini\n")
                continue
            
            # Process with AI
            print(f"{Fore.YELLOW}[AI]{Style.RESET_ALL} Thinking...", end='\r')
            response = brain.process_input(user_input)
            print(" " * 50, end='\r')  # Clear "Thinking..." message
            
            # Display response
            print(f"{Fore.RED}Central AI >{Style.RESET_ALL} {response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}[SYSTEM]{Style.RESET_ALL} Interrupted by user")
            print(f"{Fore.GREEN}Terima kasih sudah menggunakan Central AI! Sampai jumpa!{Style.RESET_ALL}\n")
            break
        except Exception as e:
            print(f"\n{Fore.RED}[ERROR]{Style.RESET_ALL} Terjadi kesalahan: {str(e)}\n")
            if config.DEBUG_MODE:
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    main()
