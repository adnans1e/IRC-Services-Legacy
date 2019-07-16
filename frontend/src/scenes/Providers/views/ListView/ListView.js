import React, { useEffect, useState } from 'react';
// import { textFilter } from 'react-bootstrap-table2-filter';
import List from '../../../../components/views/List/List';
import api from '../../api';

import './ListView.scss';

const ListView = props => {
	const columns = [
		{
			dataField: 'id',
			text: 'ID',
			sort: true
		}, {
			dataField: 'name',
			text: 'Name',
			sort: true,
			// filter: textFilter()
		}
	];

	const [data, setData] = useState([]);

	const rowEvents = {
		onClick: (e, row, rowIndex) => props.history.push(`/providers/${row.id}`)
	};
	
	useEffect(() => {
		(async function fetchData() {
			const response = await api.providers.listAll();
			setData(response.map(e => ({id: e.id, name: e.name})));
			console.log(response);
		})();
	}, []);

	return (
		<div className='ListView'>
			<h2>PROVIDERS</h2>
			<List {...props} data={data} columns={columns} rowEvents={rowEvents}/>
		</div>
	);
}

export default ListView;