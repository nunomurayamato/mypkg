# メモリの使用量を送信  

![test](https://github.com/nunomurayamato/mypkg/actions/workflows/test.yml/badge.svg)

## 概要

- このプログラムはROS2用のパッケージです。
- システムのメモリ使用率の情報を取得しパブリッシュします。

## ノード概要

- このパッケージは　メモリ使用を定期的にパブリッシュする`memorypublisher` ノードで構成されています。 
- トピック名　memory usage

## 使用方法

- `memorypublisher`の実行
-  ```
   $ ros2 run mypkg memorypublisher
   ```
  
-  ```
   $ ros2 topic echo /memory_usage
   ```

## 出力例


-  ```
   data: 42.47265625  
   ---
   data: 42.47265625  
   ---
   data: 42.47265625  
   ---
   data: 42.47265625
   ```

## テスト環境

- Ubuntu 20.04
- ros2 version humble

## ライセンス

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- © 2025 yamato nunomura

