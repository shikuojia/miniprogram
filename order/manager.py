from application import app,manager
from flask_script import Server


#web server settings
manager.add_command('run_server')




def main():
    app.run(host='0.0.0.0' ,debug=True)

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main())
        
    except Exception as e:
        import traceback
        traceback.print_exc()