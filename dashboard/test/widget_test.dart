import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:dashboard/main.dart';
import 'package:dashboard/asset_data.dart';
import 'package:dashboard/daily_value.dart';

void main() {
  test('calcTotalValue should correctly calculate total value of assets', () {
    const sameDate = '1969-07-20 20:18:04Z';
    var assets = [
      AssetData('asset1', [DailyValue(sameDate, 100)]),
      AssetData('asset2', [DailyValue(sameDate, 200)]),
      AssetData('asset3', [DailyValue(sameDate, 300)])
    ];

    var total = calcTotalValue(assets);
    expect(total, equals(600));
  });

  test('sortAsset should sort assets in descending order by last value', () {
    const sameDate = '1969-07-20 20:18:04Z';
    var assets = [
      AssetData('asset1', [DailyValue(sameDate, 100)]),
      AssetData('asset3', [DailyValue(sameDate, 300)]),
      AssetData('asset2', [DailyValue(sameDate, 200)])
    ];

    var sorted = sortAsset(assets);
    expect(sorted[0].name, equals('asset3'));
    expect(sorted[1].name, equals('asset2'));
    expect(sorted[2].name, equals('asset1'));
  });
}
