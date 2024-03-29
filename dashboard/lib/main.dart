import 'package:dashboard/asset_data.dart';
import 'package:dashboard/asset_data_repository.dart';
import 'package:dashboard/domain/authentication_service.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

import 'daily_value.dart';
import 'domain/firebase_credential.dart';
import 'repository/firestore_credential.dart';
import 'repository/firestore_datastore.dart';

void main() async {
  final credFirestore = FirestoreCredential.loadEnvironment();
  final credAuthentication = FirebaseCredential.loadEnvironment();

  WidgetsFlutterBinding.ensureInitialized();

  final firebase = await Firebase.initializeApp(
      options: FirebaseOptions(
          apiKey: credFirestore.apiKey,
          authDomain: credFirestore.authDomain,
          projectId: credFirestore.projectId,
          storageBucket: credFirestore.storageBucket,
          messagingSenderId: credFirestore.messagingSenderId,
          appId: credFirestore.appId));

  final auth = FirebaseAuth.instanceFor(app: firebase);
  await AuthenticationService(auth, credAuthentication).signInWithGoogle();

  runApp(const MyApp());
}

int calcTotalValue(List<AssetData> assets) {
  var sum = 0;
  for (var element in assets) {
    sum = sum + element.data.last.value;
  }
  return sum;
}

List<AssetData> sortAsset(List<AssetData> assets) {
  var sorted = assets.toList(growable: false);
  sorted.sort(((a, b) => b.data.last.value.compareTo(a.data.last.value)));
  return sorted;
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
      ),
      home: const MyHomePage(title: 'SBI Selenium dashboard'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;

  const MyHomePage({super.key, required this.title});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final AssetDataRepository _repository =
      FirestoreDataStore(); // SampleRepository();
  List<AssetData> _assets = List.empty();

  _MyHomePageState();

  @override
  void initState() {
    _repository.query().then(((value) => setState(() {
          _assets = value;
        })));
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final assetSortedByLastValue = sortAsset(_assets);
    final total = calcTotalValue(_assets);
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            SfCircularChart(
              title: ChartTitle(text: "Latest asset values"),
              legend: Legend(isVisible: true),
              tooltipBehavior: TooltipBehavior(enable: true),
              series: <CircularSeries>[
                PieSeries<AssetData, String>(
                    dataSource: assetSortedByLastValue,
                    xValueMapper: (datum, index) => datum.name,
                    yValueMapper: (datum, index) => datum.data.last.value,
                    dataLabelSettings: const DataLabelSettings(isVisible: true))
              ],
              annotations: [
                CircularChartAnnotation(
                    widget: Text(
                  total.toString(),
                  style: const TextStyle(
                      color: Color.fromRGBO(0, 0, 0, 0.5), fontSize: 25),
                ))
              ],
            ),
            SfCartesianChart(
                primaryXAxis: CategoryAxis(),
                title: ChartTitle(text: 'My Assets'),
                legend: Legend(isVisible: true),
                // Enable tooltip
                tooltipBehavior: TooltipBehavior(enable: true),
                series: assetSortedByLastValue
                    .map<ChartSeries<DailyValue, String>>(
                      (e) => LineSeries(
                          dataSource: sortByTime(e.data),
                          xValueMapper: ((DailyValue datum, index) =>
                              "${datum.date.month}/${datum.date.day}"),
                          yValueMapper: ((DailyValue datum, index) =>
                              datum.value),
                          name: e.name,
                          dataLabelSettings:
                              const DataLabelSettings(isVisible: true)),
                    )
                    .toList())
          ],
        ),
      ),
    );
  }

  List<DailyValue> sortByTime(List<DailyValue> original) {
    original.sort(((a, b) => a.date.millisecondsSinceEpoch
        .compareTo(b.date.millisecondsSinceEpoch)));
    return original;
  }
}
