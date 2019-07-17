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
		}, {
			dataField: 'email',
			text: 'email',
			sort: true,
		}, {
			dataField: 'groups',
			text: 'Groups',
			sort: true,
		}
	];

	const [data, setData] = useState([]);

	const rowEvents = {
		onClick: (e, row, rowIndex) => props.history.push(`/users/${row.id}`)
	};
	
	useEffect(() => {
		(async function fetchData() {
			const response = await api.users.listAll();
			setData(response.map(e => ({
				id: e.id,
				name: `${e.name} ${e.surname}`,
				email: e.email,
				groups: e.groups
			})));
			console.log(response);
		})();
	}, []);

	return (
		<div className='ListView'>
			<h2>Users</h2>
			<List {...props} data={data} columns={columns} rowEvents={rowEvents}/>
		</div>
	);
}

export default ListView;