# image_processing2
- プログラムの概要(Program outline)
  - OpenCV等で画像を取得し，フーリエ変換・逆変換をリアルタイムに行う
  - マウスで周波数を指定する（周波数フィルタリング）

- プログラムの説明(explaination of the python code)
  - 1-4行目: 必要なモジュールをimport
  - 8行目: 画像を読み込み
  - 9行目: 読み込んだ画像の大きさを取得
  - 12-15行目: フーリエ変換を実装
  - 17-19行目: 読み込んだ画像を表示
  - 21-24行目: フーリエ変換した画像を表示
  - 26-29行目: リアルタイムで逆変換した画像を表示させるための準備
  - 31-34行目: 再構築した画像を表示 
  - 36-39行目: マウスで指定した場所を表示させるための準備
  - 41行目: 複素数を代入させるための準備
  - 41-70行目: マウスがクリックされた時に実行する関数
  - 73-78行目: 右クリックされると終了

- 使い方(How to use)
  - $ python3.7 DFT.pyで実行
  - 画像が表示され，画像の一部を選択すると，その部分の逆変換がリアルタイムで表示される．
  - 右クリックがされるとプログラムは終了する．
  
- 実行結果(Execution result)
  - ![GIF](https://github.com/acaptakiyudin04/image_processing2/blob/master/gif2.gif)
 
- 参考文献(references)
  - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
  - https://www.youtube.com/watch?v=qB0cffZpw-A
  - https://www.youtube.com/watch?v=SWgrAQFHgVQ
  - http://www.s12600.net/psy/etc/python.html
  - http://whitecat-student.hatenablog.com/entry/2016/11/09/225631
