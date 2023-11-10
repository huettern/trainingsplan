/*
* @Author: Noah Huetter
* @Date:   2020-10-19 08:45:40
* @Last Modified by:   Noah Huetter
* @Last Modified time: 2020-10-19 12:02:20
*/

class Trainingsplan {

	constructor() {
		this.initial = [{ 'group': 0, 'event': 5 }, { 'group': 1, 'event': 4 }, { 'group': 2, 'event': 1 }, { 'group': 3, 'event': 3 }];

		this.startDate = '08.08.2022';
		this.trainingDays = [0, 4];
		this.trainingsPerWeek;
		this.eventsPerDay = 3;
		this.groups = ['K1', 'K2', 'K5', 'KG'];
		this.skipLastEvent = [false, false, false, true];
		this.events = ['Bo', 'Sr', 'Sp', 'Ba', 'Re', 'Tr'];
		this.warmup = ['Adi', 'Nicola']
		this.weeklyIncrement = 2;
		this.halls = [['RE', 'TR', 'BO', 'SR'], ['BA', 'SP']];
		this.specials = [{ 'id': 'airtrack', 'period': 4 }];
		this.competitionTraining = [('K1', 'RE'), ('K2', 'SP'), ('K3', ' SR'), ('K5+', 'BO')];

		this.trainingsPerWeek = this.trainingDays.length;
		// offset is in unit [training number], not days!
		// this.currentOffset = this.startDateToOffset(moment("26.10.2020", "DD.MM.YYYY").format("DD.MM.YYYY"))
		this.currentOffset = this.startDateToOffset(moment().format("DD.MM.YYYY"))
	}

	getTrainingMap(initial, rotation) {
		return initial.map(training => {
			return {
				'group': training.group,
				'event': (training.event + rotation) % (this.skipLastEvent[training.group] ? (this.events.length - 1) : this.events.length)
			};
		});
	}

	getEventByGroup(initial, rotation, group) {
		let trainingMap = this.getTrainingMap(initial, rotation)
		let training = trainingMap.find(training => training.group === group);
		return this.events[training.event];
	}

	getDateFromOffset(offset) {
		var off = moment(this.startDate, "DD.MM.YYYY");
		var dt_days = 7 * Math.floor(offset / this.trainingsPerWeek) + this.trainingDays[(offset % this.trainingsPerWeek)];
		return off.add('days', dt_days).toDate();
	}

	getTrainingInitial(initial, offset, weekly_incr) {
		let n_weeks = Math.floor(offset / this.trainingsPerWeek);
		let remainder = offset % this.trainingsPerWeek;
		let inc = n_weeks * (weekly_incr + this.trainingsPerWeek * this.eventsPerDay) + remainder * this.eventsPerDay;

		// console.log(`inc for offset ${offset} = ${inc} (${n_weeks} weeks, ${remainder} days)`)

		return initial.map(training => {
			return {
				'group': training.group,
				'event': (training.event + inc) % this.events.length
			};
		});
	}

	startDateToOffset(date) {
		var now = moment(date, "DD.MM.YYYY");
		var off = moment(this.startDate, "DD.MM.YYYY");
		var delta = now - off;
		return Math.floor(delta / (1000 * 60 * 60 * 24) / 7) * this.trainingsPerWeek;
	}

	genWeek(mapping, offset) {
		let initial = tp.getTrainingInitial(mapping, offset, tp.weeklyIncrement);

		let warm0 = this.warmup[offset % this.warmup.length];
		let warm1 = this.warmup[(offset + 1) % this.warmup.length];
		let options = { weekday: 'long', month: 'short', day: 'numeric', year: 'numeric' };
		let monday = tp.getDateFromOffset(offset).toLocaleString('de-CH', options);
		let friday = tp.getDateFromOffset(offset + 1).toLocaleString('de-CH', options);
		let group0 = this.groups[0];
		let group1 = this.groups[1];
		let group2 = this.groups[2];
		let group3 = this.groups[3];
		let g0e0 = this.getEventByGroup(initial, 0, 0);
		let g0e1 = this.getEventByGroup(initial, 1, 0);
		let g0e2 = this.getEventByGroup(initial, 2, 0);
		let g0e3 = this.getEventByGroup(initial, 3, 0);
		let g0e4 = this.getEventByGroup(initial, 4, 0);
		let g0e5 = this.getEventByGroup(initial, 5, 0);
		let g1e0 = this.getEventByGroup(initial, 0, 1);
		let g1e1 = this.getEventByGroup(initial, 1, 1);
		let g1e2 = this.getEventByGroup(initial, 2, 1);
		let g1e3 = this.getEventByGroup(initial, 3, 1);
		let g1e4 = this.getEventByGroup(initial, 4, 1);
		let g1e5 = this.getEventByGroup(initial, 5, 1);
		let g2e0 = this.getEventByGroup(initial, 0, 2);
		let g2e1 = this.getEventByGroup(initial, 1, 2);
		let g2e2 = this.getEventByGroup(initial, 2, 2);
		let g2e3 = this.getEventByGroup(initial, 3, 2);
		let g2e4 = this.getEventByGroup(initial, 4, 2);
		let g2e5 = this.getEventByGroup(initial, 5, 2);
		let g3e0 = this.getEventByGroup(initial, 0, 3);
		let g3e1 = this.getEventByGroup(initial, 1, 3);
		let g3e2 = this.getEventByGroup(initial, 2, 3);
		let g3e3 = this.getEventByGroup(initial, 3, 3);
		let g3e4 = this.getEventByGroup(initial, 4, 3);
		let g3e5 = this.getEventByGroup(initial, 5, 3);

		const template = `
        <table class="table table-hover tpl" id="table-trainingsplan">
		<thead>
		<tr>
		<th scope="col"></th>
		<th scope="col" colspan="5" class="tpl-day border-left">${monday}</th>
		<th scope="col" colspan="3" class="tpl-day border-left border-right">${friday}</th>
		</tr>
		</thead>
		<tbody>
		<tr>
		<th scope="row">${group0}</th>
		<td class="border-left">${g0e0}</td>
		<td class="">${g0e1}</td>
		<td class="">${g0e2}</td>
		<td class=""></td>
		<td class=""></td>
		<td class="border-left">${g0e3}</td>
		<td class="">${g0e4}</td>
		<td class="border-right">${g0e5}</td>
		</tr>
		<tr>
		<th scope="row">${group1}</th>
		<td class="border-left">${g1e0}</td>
		<td class="">${g1e1}</td>
		<td class="">${g1e2}</td>
		<td class=""></td>
		<td class=""></td>
		<td class="border-left">${g1e3}</td>
		<td class="">${g1e4}</td>
		<td class="border-right">${g1e5}</td>
		</tr>
		<tr>
		<th scope="row">${group2}</th>
		<td class="border-left">${g2e0}</td>
		<td class="">${g2e1}</td>
		<td class="">${g2e2}</td>
		<td class=""></td>
		<td class=""></td>
		<td class="border-left">${g2e3}</td>
		<td class="">${g2e4}</td>
		<td class="border-right">${g2e5}</td>
		</tr>
		<tr id='spannreck-search'>
		<th scope="row">${group3}</th>
		<td class="border-left">${g3e0}</td>
		<td class="">${g3e1}</td>
		<td class="">${g3e2}</td>
		<td class="">${g3e3}</td>
		<td class="">${g3e4}</td>
		<td class="border-left">${g3e3}</td>
		<td class="">${g3e4}</td>
		<td class="border-right">${g3e5}</td>
		</tr>
		<tr>
		<th scope="row"></th>
		<th scope="col" colspan="5" class="tpl-warmup border-left">${warm0}</th>
		<th scope="col" colspan="3" class="tpl-warmup border-left border-right">${warm1}</th>
		</tr>
		</tbody>
		</table>
        `;

		return template;
	}
}

const tp = new Trainingsplan();

function isMonday() {
	let dow = (moment().weekday() + 6) % 7;
	return dow == 0;
}

function isFriday() {
	let dow = (moment().weekday() + 6) % 7;
	return dow == 4;
}

function render() {
	document.getElementById("trainingsplan").innerHTML = tp.genWeek(tp.initial, tp.currentOffset);

	// emphasize day
	let off_today = tp.startDateToOffset(moment().format("DD.MM.YYYY"));
	if (off_today == tp.currentOffset) {
		let dow = (moment().weekday() + 6) % 7;
		let i = 0;
		for (const m in tp.trainingDays) {
			if (tp.trainingDays[m] == dow) {
				document.getElementsByClassName('tpl-day')[i].classList.add('table-primary');
				break;
			}
			i += 1;
		}
	}

	// specials
	for (const m in tp.specials) {
		if ((tp.currentOffset / tp.trainingsPerWeek) % tp.specials[m].period == 0) {
			document.getElementById(tp.specials[m].id).style.display = '';
		}
		else {
			document.getElementById(tp.specials[m].id).style.display = 'none';
		}
	}

	// spannreck
	document.getElementById('spannreck').style.display = 'none';
	var table = document.getElementById("table-trainingsplan");
	for (var i = 0, row; row = table.rows[i]; i++) {
		if (table.rows[i].innerHTML.includes('KG')) {
			for (var j = 0, col; col = row.cells[j]; j++) {
				if (row.cells[j].innerHTML.includes('Re')) {
					row.cells[j].classList.add("alert-warning");
					if (isMonday() && j < 4) document.getElementById('spannreck').style.display = '';
					if (isFriday() && j >= 4) document.getElementById('spannreck').style.display = '';
				}
			}
		}
	}

}

$(document).ready(function () {
	console.log("Hello World!");
	// console.log(tp.startDate);
	// let options = {weekday: 'long', month: 'short', day: 'numeric', year: 'numeric' };
	// console.log(tp.getDateFromOffset(1).toLocaleString('de-CH', options));

	// console.log(tp.initial)
	// console.log(tp.getTrainingMap(tp.initial, 0));

	// console.log(tp.getEventByGroup(tp.initial, 0, 0));
	// console.log(tp.getEventByGroup(tp.initial, 1, 0));
	// console.log(tp.getEventByGroup(tp.initial, 2, 0));
	// console.log(tp.getEventByGroup(tp.initial, 3, 0));
	// console.log(tp.getEventByGroup(tp.initial, 4, 0));
	// console.log(tp.getEventByGroup(tp.initial, 5, 0));

	// console.log(tp.startDateToOffset('22.10.2020'));

	// console.log(tp.getTrainingInitial(tp.initial, 2, tp.weeklyIncrement));

	// console.log(moment().format("DD.MM.YYYY"));

	render();
	document.getElementById("btn-left").disabled = true;
});


function btnPrevWeek() {
	if (document.getElementById("btn-left").disabled) return;
	tp.currentOffset = tp.currentOffset - tp.trainingsPerWeek;
	render();
	if (tp.currentOffset < 2) {
		document.getElementById("btn-left").disabled = true;
	}
}

function btnNextWeek() {
	tp.currentOffset = tp.currentOffset + tp.trainingsPerWeek;
	render();
	document.getElementById("btn-left").disabled = false;
}
