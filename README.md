# ROS2　メモリの使用量
![test](https://github.com/nunomurayamato/mypkg/actions/workflows/test.yml/badge.svg)

## 概要

- このプログラムはROS2用のパッケージです。

## ノード

- 現在のパソコンのメモリの使用量を表示します。 
- トピック名　memory usage

## 使用方法

- ワークスペースにパッケージをクローンし、ビルドします。
- `$ cd ~/ros2_ws/src  
   $ git clone https://github.com/nunomurayamato/mypkg.git  
   $ cd ~/ros2_ws  
   $ colcon build`

- 送信側
- `$ ros2 run mypkg Memorypublisher`

- 受信側  
- `$ ros2 topic echo /memory_usage`

## 実行例

- 送信側
- `[INFO] [1736017209.059876758] [memory_publisher]: Memory Publisher Node has been started.  
   [INFO] [1736017210.055585014] [memory_publisher]: Publishing memory usage: 42.27 MB  
   [INFO] [1736017211.055718480] [memory_publisher]: Publishing memory usage: 42.27 MB  
   [INFO] [1736017212.055796343] [memory_publisher]: Publishing memory usage: 42.27 MB  
   [INFO] [1736017213.055281600] [memory_publisher]: Publishing memory usage: 42.27 MB`

- 受信側
- `data: 42.47265625  

   data: 42.47265625  

   data: 42.47265625  

   data: 42.47265625`



## 必要なソフトウェア

- Python:テスト済みバージョン3.7, 3.8, 3.9, 3.10
- ROS2 Foxy

## テスト環境

- Ubuntu 20.04

## ライセンス

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- このパッケージのテストに利用したコンテナは下記のリンクのものを、本人の許可を得て使用しています.
 - ryuichiueda/ubuntu22.04-ros2:latest
- © 2025 yamato nunomuri

