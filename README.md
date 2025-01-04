# ROS2　メモリの使用量
![test](https://github.com/nunomurayamato/mypkg/actions/workflows/test.yml/badge.svg)

## 概要

- このプログラムはROS2用のパッケージです。

## ノード

- 現在のパソコンのメモリの使用量を表示します。 

## 使用方法

- ワークスペースにパッケージをクローンし、ビルドします。
- `$ cd ~/ros2_ws/src
   $ git clone https://github.com/nunomurayamato/mypkg.git
   $ cd ~/ros2_ws
   $ colcon build`

- 送信側
- `$ ros2 run mypkg Memorypublisher.py`

- 受信側  
- `$ ros2 topic echo /memory_usage`

- 実行例
- ``

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

