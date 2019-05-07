# Installation and Usage

* 環境
    * python 3.7(venv)
    * diango 2.2.1
    * django-allauth 0.39.1
    * django-bootstrap4 0.0.8 #使わないかも
    * django-bootstrap-modal-forms
    * django-pure-pagination

* インストール
    * python3.xをインストール
    * pip -r requirements.txt
    
* 動作確認
    * anitya-syntheticsのPJフォルダへ移動する
    * python manage.py migrate
    * python manage.py createsuperuser
    * pip manage.py runserver 0:8000
    * http://<ローカル環境の任意のIP>:8000 へアクセスする
