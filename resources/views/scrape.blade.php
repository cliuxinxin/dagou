@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>城市</th>
                    <th>网址</th>
                    <th>最新抓取数目</th>
                    <th>最新抓取时间</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td>{{$item->name}}</td>
                        <td  class="hideOverflow"><a href="{{$item->url}}">{{$item->url}}</a></td>
                        <td>{{$item->insert_numbers}}</td>
                        <td>{{$item->time}}</td>
                    </tr>
                @endforeach
            </table>
        </div>
        {{ $items->links() }}
    </div>
    </div>
@endsection
